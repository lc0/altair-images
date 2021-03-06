from setuptools import find_packages, setup

with open("readme.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="altair-images",
    version="0.1.4",
    author="Sergii Khomenko",
    description="Serving interactive charts with images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lc0/altair_images",
    classifiers=[
        "Development Status :: 4 - Beta ",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='altair flask colab ngrok demo',
    install_requires=required,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)