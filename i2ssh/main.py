#!/usr/bin/env python
import argparse
import os
import logging
import sys
import yaml
from layout import Layout
from applescript import launch

DEFAULT_CONFIG = '~/.i2sshrc'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'cluster',
            help='the cluster to connect to.')
    parser.add_argument(
            '-c', '--config', default=DEFAULT_CONFIG,
            help='the config file to use (default "%s").' % DEFAULT_CONFIG)
    parser.add_argument(
           '-v', '--verbose', action='store_true', default=False,
            help='increases log verbosity.')
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    config_path = os.path.expanduser(args.config)
    if not os.path.exists(config_path):
        logging.error('No config file at %s', config_path)
        sys.exit(0)

    logging.debug('Load %s from %s' % (args.cluster, config_path))
    with open(config_path, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

        if not args.cluster in cfg:
            logging.error('%s is not a cluster in %s', args.cluster, config_path)
            sys.exit(0)

        cluster_config = cfg[args.cluster]
        logging.debug('Cluster config: %s', cluster_config)

        layout = Layout(cluster_config)
        logging.debug('Layout: %s', layout)

        launch(layout, cluster_config)

if __name__ == '__main__':
    main()
