I2SSH
=====

SSH into to a cluster of machines using `iTerm 2 <http://www.iterm2.com>`_ split panes on OSX.

|buildstatus|_

Usage
*****

::

    $ cat ~/.i2sshrc
    ---
    version: 1
    mycluster:
      hosts:
        - host1.domain.net
        - host2.domain.net
        - host3.domain.net
        - host4.domain.net

    $ i2ssh mycluster


Command-line arguments
**********************

::

    $ i2ssh -h
    usage: i2ssh [-h] [-c CONFIG] [-v] cluster

    positional arguments:
      cluster               the cluster to connect to.

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            the config file to use (default "~/.i2sshrc").
      -v, --verbose         increases log verbosity.


Config file
***********

::

    ---
    version: 1
    mycluster:
      cmd: 'ssh'        # the command to execute in every pane, defaults to 'ssh'
      layout: '2x2'     # how to split the window, defaults '(n+1/2) x (n/2)'
      hosts:
        - host1.domain.net
        - host2.domain.net
        - host3.domain.net
        - host4.domain.net


.. |buildstatus| image:: https://api.travis-ci.org/mbruggmann/i2ssh.png?branch=master
.. _buildstatus: https://travis-ci.org/mbruggmann/i2ssh
