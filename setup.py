#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

PACKAGES = ['pyipa']
SCRIPTS = ['bin/pyipa']

def get_init_val(val, packages=PACKAGES):
    pkg_init = "%s/__init__.py" % PACKAGES[0]
    value = '__%s__' % val
    fn = open(pkg_init)
    for line in fn.readlines():
        if line.startswith(value):
            return line.split('=')[1].strip().strip("'")


setup(
    name='pyipa',
    version=get_init_val('version'),
    description=get_init_val('description'),
    long_description=open('README.rst').read(),
    author=get_init_val('author'),
    url=get_init_val('url'),
    package_data={'': ['LICENSE', 'NOTICE']},
    license=get_init_val('license'),
    install_requires = ['docopt'],
    packages=PACKAGES,
    scripts=SCRIPTS
)
