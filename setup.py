#!/usr/bin/env python
#
# Hannes Hapke - Santiago, Chile - 2014
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

"""
Distutils setup script for pynrelutility.

"""


import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from __version__ import VERSION

setup(
    name='pynrelutility',
    version=VERSION,
    author='Hannes Hapke',
    author_email='hannes@renooble.com',
    url='https://github.com/hanneshapke/pynrelutility',
    download_url='https://github.com/hanneshapke/pynrelutility/archive/master.zip',
    description='Python interface for NREL\'s Utility API API. The API is providing \
                utility names and rates for a given location',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r').read(),
    py_modules=['nrel_utility', 'nrel_utility_errors', '__version__'],
    provides=['nrel_utility'],
    requires=['requests'],
    install_requires=['requests >= 2.2.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering',
    ],
    keywords='nrel utility energy electricity rates api json US',
    license='MIT',
)