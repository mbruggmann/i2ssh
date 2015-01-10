I2SSH
=====

SSH into to a cluster of machines using [iTerm 2][] split panes on OSX.

### Usage

```bash
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
```

### Configuration parameters

```bash
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
```


[iTerm 2]: http://www.iterm2.com/
