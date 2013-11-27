import sleekxmpp
import inspect
from config import configuration

class Jabber(sleekxmpp.ClientXMPP):
    name = 'jabber_xmpp'
    keyword = 'jabber'

    def __init__(self):
        jid = configuration.get('xmpp_username')
        password = configuration.get('xmpp_password')

        super(Jabber, self).__init__(jid, password)
        self.add_event_handler('session_start', self.start)

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, Jabber):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another instance of Jabber running!")

        host = configuration.get('xmpp_server_host')
        port = configuration.get('xmpp_server_port')

        if self.connect((host, port)):
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
        print "Closing XMPP Connection"
        self.disconnect(wait=False)
        
    def start(self, event):
        self.send_presence()
        self.get_roster()

    def send_recipients(self, message):
        recipient = configuration.get('xmpp_recipients')

        self.send_message(mto=recipient, mbody=message)

class PluginError(Exception):
    pass

Plugin = Jabber
