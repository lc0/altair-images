# Serving interactive charts with images - based on Altair
[![PyPI version](https://badge.fury.io/py/altair-images.svg)](https://pypi.org/project/altair-images/)
[![Downloads](https://pepy.tech/badge/altair-images)](https://pepy.tech/project/altair-images)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lc0/altair-images/blob/master/examples/colab.ipynb)

Project fully supports Google Colab. For more details see [examples](examples/)

## Installation
```sh
pip install altair-images
```

## How to use
```python
import numpy as np

from altair_images import plot_with_image

embedding_data = np.load('../tests/pca_data_100.npy')
sample_images = np.load('../tests/sample_images_100.npy')
labels = np.load('../tests/sample_labels_100.npy')

plot_with_image(embedding_data, labels, sample_images)
```

![Fashion MNIST embeddings](https://raw.githubusercontent.com/lc0/altair-images/master/altair-images.gif)

## TODO
- [x] Add examples in readme
- [x] Add CI for tagging and publishing new version from master
- [ ] Add tests
- [ ] Example of line_plot and pictures(speed and frame, weight and body)
