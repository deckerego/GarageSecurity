import sleekxmpp
import inspect
import logging
import datetime
from config import configuration
from vision import Vision

logger = logging.getLogger('garagesec')
#FIXME There is definitely a better way to share a vision service than to have two running instantiations....
vision_service = Vision(configuration.get('webcam_host'), configuration.get('webcam_port'))

class Jabber(sleekxmpp.ClientXMPP):
    name = 'jabber_xmpp'
    keyword = 'jabber'

    def __init__(self, jid, password):
        super(Jabber, self).__init__(jid, password)

        self.last_alert = None
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.receive)

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

        if self.connect((host, port)):
            logger.info("Opened XMPP Connection")
            self.process(block=False)
        else:
            raise Exception("Unable to connect to Google Jabber server")

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

    def send_recipients(self, body):
        #FIXME It's rather ridiculous to maintain the last alert timestamp in two places
        self.last_alert = datetime.datetime.now()

        message = self.Message()
        message['to'] = configuration.get('xmpp_recipients')
        message['type'] = 'chat'
        message['body'] = body

        logger.debug("Sending message: %s" % message)
        message.send()

    def receive(self, message):
        if message['type'] in ('chat', 'normal'):
            logger.debug("XMPP Message: %s" % message)

            if 'door' in message['body'].lower():
                template_image = configuration.get('vision_template_image')
                template_coords = configuration.get('vision_template_coords')
                template_margin = configuration.get('vision_template_margin')
                
                is_closed, location = vision_service.look_if_closed(template_image, template_coords, template_margin)
                message.reply("Door is closed: %s" % is_closed).send()
            elif 'status' in message['body'].lower():
                message.reply("Last alert: %s" % self.last_alert).send()
            else:
                message.reply("Command not found: %(body)s" % message).send()

class PluginError(Exception):
    pass

Plugin = Jabber
