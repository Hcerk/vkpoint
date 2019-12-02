#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import open
from setuptools import setup

"""
:authors: Hcerk
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2019 Hcerk
"""


version = '2.0.5'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'vkpoint_api',
    version = version,

    author = 'Hcerk',

    description=(
        u'vkpoint - это python модуль для работы с монетой VK Point (VK Point API wrapper)'
    ),
    
    long_description=  long_description,
    long_description_content_type = 'text/markdown',

    url = 'https://github.com/Hcerk/vkpoint',
    download_url = f'https://github.com/Hcerk/vkpoint/archive/v{version}.zip',

    license = 'Apache License, Version 2.0, see LICENSE file',

    packages = ['vkpoint_api'],
    install_requires = ['requests', 'six'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
