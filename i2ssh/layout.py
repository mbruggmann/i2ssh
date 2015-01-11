#!/usr/bin/env python
from math import ceil, sqrt

class Layout:
    '''Describes an iTerm2 split layout.'''

    def __init__(self, config):
        nr_hosts = len(config['hosts'])
        if 'layout' in config:
            self._cols, self._rows = map(int, config['layout'].split('x'))
        else:
            self._cols, self._rows = self._default_layout(nr_hosts)
        self._disabled = self.cols*self.rows - nr_hosts

    @property
    def cols(self):
        return self._cols

    @property
    def rows(self):
        return self._rows

    @property
    def disabled(self):
        return self._disabled

    def _default_layout(self, nr_panes):
        '''Compute the default layout, based on the number of panes'''
        cols = max(int(ceil(sqrt(nr_panes))), 1)
        rows = max(int(ceil(float(nr_panes)/cols)), 1)
        return (cols, rows)

    def __str__(self):
        return '%sx%s' % (self.cols, self.rows)
