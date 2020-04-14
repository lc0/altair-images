"""
Serve images
"""
from typing import Callable

import io

from flask_cors import CORS
from PIL import Image
from flask import Flask, send_file

# TODO: type for flask app
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
        # convert numpy array to PIL Image
        img = Image.fromarray()
        if to_rgb:
            img = img.convert('RGB')

        # create file-object in memory
        file_object = io.BytesIO()

        # write PNG in file-object
        img.save(file_object, 'PNG')

        # move to beginning of file so `send_file()` it will read from start
        file_object.seek(0)

        return send_file(file_object, mimetype='image/PNG')

    return app


# def serve_images(
#     image_transform_func,
#     to_rgb=True,
#     host='127.0.0.1',
#     port=5555
# )

if __name__ == "__main__":
    import numpy as np

    sample_images = np.load('tests/sample_images_100.npy')

    image_func = lambda image_id: sample_images[image_id].reshape(28, 28)*255
    app = _create_flask_app(sample_images, image_func)

    app.run()