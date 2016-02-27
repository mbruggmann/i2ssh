#!/usr/bin/env python
import os
import logging
import sys
import yaml

class Config:
    '''Parses the i2sshrc config file.'''

    def __init__(self, path=None):
        config_path = os.path.expanduser(path)
        if not os.path.exists(config_path):
            logging.error('No config file at %s', config_path)
            sys.exit(0)

        with open(config_path, 'r') as ymlfile:
            self._cfg = yaml.load(ymlfile)

    def cluster(self, name):
        if not name in self._cfg:
            logging.error('%s is not a cluster in %s', args.cluster, config_path)
            sys.exit(0)

        return self._cfg[name]

    def clusternames(self):
        """Return the names of the clusters in the config file"""
        return self._cfg.keys()

