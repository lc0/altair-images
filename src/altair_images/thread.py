import threading

from werkzeug.serving import make_server
from flask_ngrok import _run_ngrok


class ServerThread(threading.Thread):

    def __init__(self, app, host, port):
        threading.Thread.__init__(self)
        self.srv = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()

def start_flask_thread(server_thread, app, host='0.0.0.0', port=5555, use_ngrok=False):
    if server_thread:
        print(" * Stopping current thread")
        server_thread.shutdown()

    # running fist time, so we should start ngrok
    # TODO: check on what port we have running ngrok's
    if server_thread is None and use_ngrok:
            ngrok_address = _run_ngrok(port)
            print(f" * Running on {ngrok_address}")

    server_thread = ServerThread(app, host=host, port=port)
    server_thread.start()
    print(f" * Started a server thread on http://{host}:{port}")

    return server_thread