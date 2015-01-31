#!/usr/bin/env python
from collections import namedtuple
from AppKit import NSScreen

Point = namedtuple('Point', 'x, y')
Size = namedtuple('Size', 'width, height')

class Window:
    '''Describes position and size of an application window on OSX.'''

    def __init__(self, config):
        if 'window' in config:
            x, y, w, h = map(int, config['window'].split(','))
            self._origin = Point(x=x, y=y)
            self._size = Size(width=w, height=h)
        else:
            self._origin, self._size = self._default_window()

    @property
    def origin(self):
        return self._origin

    @property
    def size(self):
        return self._size

    def _default_window(self):
        '''Maximize within the available frame by default'''
        return self._available_frame()

    def _available_frame(self):
        '''The available screen frame (screen resolution - menubar and dock)'''
        frame = NSScreen.mainScreen().visibleFrame()
        origin = Point(x=frame.origin.x, y=frame.origin.y)
        size = Size(width=frame.size.width, height=frame.size.height)
        return (origin, size)

    def __str__(self):
        return '%s,%s' % (self.origin, self.size)
