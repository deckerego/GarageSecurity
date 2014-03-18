# -*- coding: utf-8 -*-

import sleekxmpp
import inspect
import logging
import datetime
from detector import Detector
from temperature import Temperature
from config import configuration

logger = logging.getLogger('basemon')

class Jabber(sleekxmpp.ClientXMPP):
    name = 'jabber_xmpp'
    keyword = 'jabber'

    def __init__(self, jid, password):
        super(Jabber, self).__init__(jid, password)

        self.temperature = None
        self.detector = None
        # FIXME It appears only one session is permitted at a time with SleekXMPP
        #self.add_event_handler('session_start', self.start)
        #self.add_event_handler('message', self.receive)

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if isinstance(other, Detector):
                self.detector = other
            elif isinstance(other, Temperature):
                self.temperature = other
            elif isinstance(other, Jabber) and other.keyword == self.keyword:
                raise PluginError("Found another instance of Jabber running!")

        host = configuration.get('xmpp_server_host')
        port = configuration.get('xmpp_server_port')

        if self.connect((host, port)):
            logger.info("Opened XMPP Connection")
            self.process(block=False)
        else:
            raise Exception("Unable to connect to Google Jabber server")

    # This is invoked within Bottle as part of each route when installed
    def apply(self, callback, route):
        args = inspect.getargspec(callback)[0]
        if self.keyword not in args:
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
        message = self.Message()
        message['to'] = configuration.get('xmpp_recipients')
        message['type'] = 'chat'
        message['body'] = body

        logger.debug("Sending message: %s" % message)
        message.send()

    def receive(self, message):
        if message['type'] in ('chat', 'normal'):
            logger.debug("XMPP Message: %s" % message)
            from_account = "%s@%s" % (message['from'].user, message['from'].domain)
            logger.info("Received message from %s" % from_account)

            if not from_account in configuration.get('xmpp_recipients'):
                logger.warn("Received message from non-whitelist user %s: %s" % (from_account, message['body']))
            elif 'basement climate' in message['body'].lower():
                humidity, celsius, status = self.temperature.get_conditions()
                farenheit = ((celsius * 9) / 5) + 32
                message.reply("%s ˚F %s Humidity" % (farenheit, humidity)).send()
            else:
                logger.info("Uncaught command from %s: %s" % (from_account, message['body']))

class PluginError(Exception):
    pass

Plugin = Jabber
