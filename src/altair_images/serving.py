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