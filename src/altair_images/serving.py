"""
Serve images
"""
from typing import Callable

import io

from flask_cors import CORS
from PIL import Image
from flask import Flask, send_file

# TODO: typehints for flask app
def _create_flask_app(image_container, image_transform_func: Callable, to_rgb=True):
    """
    Given `image_container` and `image_transform_func` creates a Flask app
    """

    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def hello():
        return "it all works fine"

    @app.route("/img/<int:image_id>.png")
    def image(image_id):
        """Serve image by image_id"""

        img = Image.fromarray(image_transform_func(image_id))
        if to_rgb:
            img = img.convert('RGB')

        file_object = io.BytesIO()
        img.save(file_object, 'PNG')
        file_object.seek(0)

        return send_file(file_object, mimetype='image/PNG')

    return app

# TODO: move start_flask_thread from my private branch
from flask_ngrok import start_flask_thread as _start_flask_thread

def _start_flask_thread(server_thread, app, host='0.0.0.0', port=5555):
    if server_thread:
        print(" * Stopping current thread")
        server_thread.shutdown()

    # running fist time, so we should start ngrok
    # TODO: check on what port we have running ngrok's
    if server_thread is None:
        ngrok_address = _run_ngrok(port)
        print(f" * Running on {ngrok_address}")

    server_thread = ServerThread(app, host=host, port=port)
    server_thread.start()
    print(f" * Started a server thread on {host}:{port}")

    return server_thread



# def serve_images(
#     image_transform_func,
#     to_rgb=True,
#     host='127.0.0.1',
#     port=5555
# )

# TODO: move nicely to tests
if __name__ == "__main__":
    import numpy as np

    sample_images = np.load('tests/sample_images_100.npy')

    # # _create_flask_app
    # image_func = lambda image_id: sample_images[image_id].reshape(28, 28)*255
    # app = _create_flask_app(sample_images, image_func)

    # app.run()