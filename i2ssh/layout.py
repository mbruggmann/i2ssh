#!/usr/bin/env python
import math

class Layout:
    '''Describes an iTerm2 split layout.'''

    def __init__(self, config):
        if 'layout' in config:
            self._cols, self._rows = map(int, config['layout'].split('x'))
        else:
            nr_panes = len(config['hosts'])
            self._cols, self._rows = self._default_layout(nr_panes)

    @property
    def cols(self):
        return self._cols

    @property
    def rows(self):
        return self._rows

    def _default_layout(self, nr_panes):
        '''Compute the default layout, based on the number of panes'''
        cols = max(int(math.ceil(math.sqrt(nr_panes))), 1)
        rows = max(int(math.floor(math.sqrt(nr_panes))), 1)
        return (cols, rows)

    def __str__(self):
        return '%sx%s' % (self.cols, self.rows)
