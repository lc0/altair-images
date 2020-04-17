import altair as alt
import numpy as np
import pandas as pd

from altair_images.serving import _create_flask_app
from altair_images.thread import start_flask_thread
from altair_images.proxy import start_ngrok


# TODO: add tearing down after us
def serve_images(sample_images, image_transform_func, host='127.0.0.1', port=5555, use_ngrok=False, to_rgb=True, server_thread=None):
    """
    Just serve images out of the box
    """

    app = _create_flask_app(sample_images, image_transform_func, to_rgb=to_rgb)
    _, serving_url = start_flask_thread(app, host=host, port=port, use_ngrok=use_ngrok)

    return serving_url


# TODO: beatiful version with just dataframe - plot_with_image(dataframe, columns, use_ngrok=False):
def plot_with_image(data, labels, sample_images, columns={}, use_ngrok=False):
    """
    Build a entire graph and simple return it
    """
    data_labels = np.vstack((data.T, labels)).T
    df = pd.DataFrame(data=data_labels, columns=['x', 'y', 'label'])

    image_func = lambda image_id: sample_images[image_id].reshape(28, 28)*255
    image_url = serve_images(sample_images, image_func, use_ngrok=use_ngrok)

    df['image_url'] = [f"{image_url}/img/{image_id}.png" for image_id in range(0, len(labels))]

    x = columns.get('x', 'x')
    y = columns.get('x', 'y')
    label = columns.get('label', 'label')

    multi_mouseover = alt.selection_multi(on='mouseover', toggle=True, empty='none')

    base = alt.Chart(df).mark_circle(radius=50).encode(
        x=f'{x}:Q',
        y=f'{y}:Q',

        color=f'{label}:N',
    ).add_selection(
        multi_mouseover
    )


    image = alt.Chart(df).mark_image(
    ).encode(
        url='image_url'
    ).transform_filter(
        multi_mouseover
    ).properties(width=100, height=100)

    return base | image