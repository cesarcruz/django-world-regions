__author__ = 'juliocesar'

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-world-regions',
    version='0.1',
    packages=['world_regions'],
    include_package_data=True,
    license="MIT License",
    description="Simple Django app to group countries in world's regions like *Northern America*, "
                "*Eastern Europe*, etc.",
    long_description=README,
    url='https://github.com/cesarcruz/django-world-regions',
    author="Julio Cesar Rodriguez",
    author_email='juliocesarrodriguezcruz@gmail.com',
    install_requires=['django-countries'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        # TODO: Test if this work in python 3 and versions older than 2.7, then include it here
    ],
)
