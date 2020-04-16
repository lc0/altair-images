import threading

from werkzeug.serving import make_server
from altair_images.proxy import start_ngrok


class ServerThread(threading.Thread):
    pool = {}

    def __init__(self, app, host, port):
        threading.Thread.__init__(self)

        if port in self.pool:
            print(" * Re-using server on the same port")
            self.srv = self.pool[port]
            self.srv.shutdown()

        self.srv = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

        self.pool[port] = self.srv



    def run(self):
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


def start_flask_thread(app, host='0.0.0.0', port=5555, use_ngrok=False):
    """
        Start Flask app in a separate thread.
    """

    # running fist time, so we should start ngrok
    if use_ngrok:
        ngrok_address = start_ngrok(port)
        print(f" * Running on {ngrok_address}")

    server_thread = ServerThread(app, host=host, port=port)
    server_thread.start()
    print(f" * Started a server thread on http://{host}:{port}")

    return server_thread, f"http://{host}:{port}"