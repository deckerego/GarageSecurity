import sleekxmpp
import inspect
import logging
import datetime
import os, time
from s3 import S3
from camera import Camera
from config import configuration

logger = logging.getLogger('garagesec')
logger.setLevel(20)

class Jabber(sleekxmpp.ClientXMPP):
  name = 'jabber_xmpp'
  keyword = 'jabber'

  def __init__(self, jid, password, camera, temperature):
    if jid and password:
        super(Jabber, self).__init__(jid, password)

    self.camera = camera
    self.temperature = temperature
    self.instance_name = None
    self.silent = True

    if jid and password:
        self.silent = False
        self.instance_name = configuration.get('instance_name').lower()
        self.add_event_handler('session_start', self.start, threaded=False, disposable=True)
        self.add_event_handler('message', self.receive, threaded=True, disposable=False)

  def __del__(self):
    self.close()

  # This is invoked when installed as a Bottle plugin
  def setup(self, app):
    self.routes = app

    for other in app.plugins:
      if not isinstance(other, Jabber):
        continue
      if other.keyword == self.keyword:
        raise PluginError("Found another instance of Jabber running!")

    host = configuration.get('xmpp_server_host')
    port = configuration.get('xmpp_server_port')

    if not host and not port:
        logger.warn("No XMPP settings defined, disabling Jabber")
        return

    if self.connect((host, port)):
      logger.info("Opened XMPP Connection")
      self.process(block=False)
    else:
      raise Exception("Unable to connect to Google Jabber server")

    self.bucket = S3()

  # This is invoked within Bottle as part of each route when installed
  def apply(self, callback, context):
    conf = context.config.get('jabber') or {}
    keyword = conf.get('keyword', self.keyword)

    args = inspect.getargspec(context.callback)[0]
    if keyword not in args:
      return callback

    def wrapper(*args, **kwargs):
      kwargs[self.keyword] = self
      rv = callback(*args, **kwargs)
      return rv
    return wrapper

  # De-installation from Bottle as a plugin
  def close(self):
    logger.info("Closing XMPP Connection")
    self.disconnect(wait=False)

  def start(self, event):
    self.send_presence()
    self.get_roster()

  def send_alert_image(self, file_path):
    if not self.silent:
      file_bin = open(file_path, 'r').read()
      file_url = self.bucket.upload(file_bin)
      self.send_alert_msg(file_url)

  def send_alert_msg(self, body):
    if not self.silent:
        for recipient in configuration.get('xmpp_recipients'):
          message = self.Message()
          message['to'] = recipient
          message['type'] = 'chat'
          message['body'] = body

          logger.debug("Sending message: %s" % message)
          message.send()

  def set_silence(self, silent):
      self.silent = silent

  def receive(self, message):
    if message['type'] in ('chat', 'normal'):
      logger.debug("XMPP Message: %s" % message)
      from_account = "%s@%s" % (message['from'].user, message['from'].domain)
      logger.info("Received message from %s" % from_account)

      if not from_account in configuration.get('xmpp_recipients'):
        logger.warn("Received message from non-whitelist user %s: %s" % (from_account, message['body']))
      elif "%s camera" % self.instance_name in message['body'].lower():
        image_bin = self.camera.get_image()
        image_url = self.bucket.upload(image_bin)
        message.reply("Status: %s" % image_url).send()
      elif "%s lastevent" % self.instance_name in message['body'].lower():
        archive_dir = configuration.get('webcam_archive')
        time_struct = max(map(lambda x: os.path.getmtime("%s/%s" % (archive_dir, x)), os.listdir(archive_dir)))
        message.reply("Last Event: %s" % time.strftime("%c", time.localtime(time_struct))).send()
      elif "%s climate" % self.instance_name in message['body'].lower():
        humidity, celsius, status = self.temperature.get_conditions()
        farenheit = ((celsius * 9) / 5) + 32
        message.reply("Temperature: %0.2fF, Humidity: %0.2f%%" % (farenheit, humidity)).send()
      elif "%s silent" % self.instance_name in message['body'].lower():
        self.silent = True
        message.reply("Silencing alerts").send()
      elif "%s audible" % self.instance_name in message['body'].lower():
        self.silent = False
        message.reply("Enabling alerts").send()
      else:
        logger.info("Uncaught command from %s: %s" % (from_account, message['body']))

class PluginError(Exception):
  pass

Plugin = Jabber
