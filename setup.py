from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="altair-images",
    version="0.0.3",
    author="Sergii Khomenko",
    description="Serving interactive charts with images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lc0/altair_images",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='altair flask colab ngrok demo',
    install_requires=required,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)