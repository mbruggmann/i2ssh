#!/usr/bin/env python
import argparse
import os
import logging
import sys
import yaml
from config import Config
from layout import Layout
from applescript import AppleScript

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

    config = Config(path=args.config).cluster(args.cluster)
    logging.debug('Cluster config: %s', config)

    layout = Layout(config)
    logging.debug('Layout: %s', layout)

    applescript = AppleScript(config, layout)
    applescript.launch()


if __name__ == '__main__':
    main()
