i2ssh
=====

ssh into to a cluster of machines using `iTerm 2 <http://www.iterm2.com>`_ split panes on OSX.

|pypi|_ |buildstatus|_

Installation
************

::

    $ pip install i2ssh


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
      -l, --list            list the clusters in the config file.


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

      # the remote user to log into as, defaults to the local user.
      user: 'username'

      # how to split the window, defaults to 'sqrt(n) x (n/cols)'.
      layout: '2x2'

      # position and size for the new window, defaults to
      # maximize within the available space on screen. the format
      # is (x, y, width, height).
      window: '0, 0, 1440, 900'

      # the time to wait between scripting commands, in seconds.
      # defaults to 0.1
      delay: 0.1

      # the list of hosts to execute the command for.
      hosts:
        - host1.domain.net
        - host2.domain.net
        - host3.domain.net
        - host4.domain.net


.. |buildstatus| image:: https://img.shields.io/travis/mbruggmann/i2ssh/master.svg
.. _buildstatus: https://travis-ci.org/mbruggmann/i2ssh
.. |pypi| image:: https://img.shields.io/pypi/v/i2ssh.svg
.. _pypi: https://pypi.python.org/pypi/i2ssh
