#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='i2ssh',
      version='0.1.0',
      description='SSH into to a cluster of machines using iTerm 2 split panes on OSX.',
      author='Marc Bruggmann',
      url='https://github.com/mbruggmann/i2ssh',
      scripts=['bin/i2ssh'],
      packages=find_packages(),
     )
