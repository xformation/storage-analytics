#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='xmldataset',
    version='1.0.1',
    description='XML Dataset: xml parsing made easy',
    long_description=readme + '\n\n' + history,
    author='James Spurin',
    author_email='james@spurin.com',
    url='https://github.com/spurin/xmldataset',
    packages=[
        'xmldataset',
    ],
    package_dir={'xmldataset': 'xmldataset'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='xmldataset',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
)
