from altair_images.serving import _create_flask_app
from altair_images.thread import start_flask_thread

# TODO: add handling in case port is used already
# TODO: add tearing down after us

def serve_images(sample_images, image_transform_func, host='127.0.0.1', port=5555, ngrok=False, to_rgb=True, server_thread=None):
    """Just serve images out of the box"""

    app = _create_flask_app(sample_images, image_transform_func, to_rgb=to_rgb)
    start_flask_thread(server_thread, app, host=host, port=port, ngrok=False)