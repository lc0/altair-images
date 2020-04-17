# place where all proxies live
import logging

from pyngrok import ngrok

class Proxy():
    pool = {}

    def __init__(self, port):

        if port in self.pool:
            logging.info(" * Re-using ngrok on the same port")
            self.public_url  = self.pool[port]
        else:
            logging.info(" * Starting a new instance of ngrok")
            self.public_url = ngrok.connect(port, "http")
            self.pool[port] = self.public_url

    def get_host(self):
        return self.public_url


# TODO: add support of configs
def start_ngrok(port: int):
    return Proxy(port).get_host()