import argparse

config_values = {
	'xmpp_server_host': '74.125.142.125',
	'xmpp_server_port': '5222',
    'xmpp_username': '',
    'xmpp_password': '',
    'xmpp_recipients': ''
}

class Configuration(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        args, _ = parser.parse_known_args()

    def get(self, name):
        return config_values.get(name)

configuration = Configuration()
