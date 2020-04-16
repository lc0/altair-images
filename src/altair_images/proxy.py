# place where all proxies live

from pyngrok import ngrok

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
    public_url = ngrok.connect(port, "http")

    return public_url