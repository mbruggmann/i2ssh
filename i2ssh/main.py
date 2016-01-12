#!/usr/bin/env python
import argparse
import os
import logging
import sys
import yaml
from config import Config
from layout import Layout
from window import Window
from applescript import AppleScript

DEFAULT_CONFIG = '~/.i2sshrc'

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
            'cluster', nargs='?',
            help='the cluster to connect to.')
    parser.add_argument(
            '-c', '--config', default=DEFAULT_CONFIG,
            help='the config file to use (default "%s").' % DEFAULT_CONFIG)
    parser.add_argument(
           '-v', '--verbose', action='store_true', default=False,
            help='increases log verbosity.')
    parser.add_argument(
            '-l', '--list', action='store_true', default=False,
            help='list the clusters in the config file.')
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    config = Config(path=args.config)

    if args.list:
        print "Clusters in %s:" % (args.config)
        for name in config.clusternames():
            print "- %s" % (name)
        return

    # need to check if this is set manually due to use of nargs=? above, which
    # seems to be only way to get an optional arg list --list to work and not
    # also require the cluster positional arg to be set
    if args.cluster is None:
        parser.error("cluster name is required")

    config = config.cluster(args.cluster)
    logging.debug('Cluster config: %s', config)

    layout = Layout(config)
    logging.debug('Layout: %s', layout)

    window = Window(config)
    logging.debug('Window: %s', window)

    applescript = AppleScript(config, layout, window)
    applescript.launch()


if __name__ == '__main__':
    main()
