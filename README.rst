I2SSH
=====

SSH into to a cluster of machines using `iTerm 2 <http://www.iterm2.com>`_ split panes on OSX.

|buildstatus|_

Usage
*****

::

    $ cat ~/.i2sshrc
    ---
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
    # the name of the cluster.
    mycluster:

      # the command to execute in every pane, defaults to 'ssh'.
      # the hostname for that pane will be appended to the
      # command before being executed, resulting in something
      # like 'ssh host1.domain.net'.
      cmd: 'ssh'

      # how to split the window, defaults to 'sqrt(n) x n/cols'.
      layout: '2x2'

      # the time to wait between scripting commands, in seconds.
      # defaults to 0.1
      delay: 0.1

      # the list of hosts to execute the command for.
      hosts:
        - host1.domain.net
        - host2.domain.net
        - host3.domain.net
        - host4.domain.net


.. |buildstatus| image:: https://api.travis-ci.org/mbruggmann/i2ssh.png?branch=master
.. _buildstatus: https://travis-ci.org/mbruggmann/i2ssh
