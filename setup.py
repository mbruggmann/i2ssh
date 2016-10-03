#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(name='i2ssh',
      version='0.4.0',
      description='SSH into to a cluster of machines using iTerm 2 split panes on OSX.',
      long_description=read('README.rst'),
      author='Marc Bruggmann',
      author_email='bruggmann.marc@gmail.com',
      url='https://github.com/mbruggmann/i2ssh',
      license='Apache License 2.0',
      packages=find_packages(),
      install_requires=['pyyaml', 'quik', 'pyobjc-framework-Cocoa'],
      tests_require=['nose', 'testfixtures', 'mock'],
      test_suite="nose.collector",
      entry_points={
        'console_scripts': [
          'i2ssh = i2ssh.main:main',
        ],
      },
      classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Operating System :: MacOS',
      ],
     )
