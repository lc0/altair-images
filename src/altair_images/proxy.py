# place where all proxies live

# TODO: if I see people using a lib, would be reasonable to write own ngrok wrapper
# For now, we just rely on private method from flask_ngrok
from flask_ngrok import _run_ngrok

class Proxy():
    pool = {}

    def __init__(self, port):

        if port in self.pool:
            print(" * Re-using ngrok on the same port")
            self.ngrok_url  = self.pool[port]
        else:
            print("every time a new one?")
            self.ngrok_url = _run_ngrok(port)[0]
            self.pool[port] = self.ngrok_url

    def get_host(self):
        return self.ngrok_url


# TODO: add support of configs
def start_ngrok(port):
    return Proxy(port).get_host()