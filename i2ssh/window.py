#!/usr/bin/env python
from collections import namedtuple

Point = namedtuple('Point', 'x, y')
Size = namedtuple('Size', 'width, height')

class Window:
    '''Describes position and size of an application window on OSX.'''

    def __init__(self, config):
        if 'window' in config:
            x, y, w, h = map(int, config['window'].split(','))
            self._origin = Point(x, y)
            self._size = Size(w, h)
        else:
            self._origin, self._size = self._default_window()

    @property
    def origin(self):
        '''The origin of the window, measure from the top left corner.'''
        return self._origin

    @property
    def size(self):
        '''The size of the window.'''
        return self._size

    def _default_window(self):
        '''Maximize within the available frame by default'''
        frame = self._osx_frame()
        visible = self._osx_available()

        width = int(visible.size.width)
        height = int(visible.size.height)

        # need to translate from x/y measured from lower left corner
        # (as reported by OSX) to upper left corner
        x = int(visible.origin.x)
        y = int(frame.size.height - visible.size.height - visible.origin.y)

        return (Point(x, y), Size(width, height))

    def _osx_frame(self):
        '''What OSX reports as the screen frame.'''
        from AppKit import NSScreen
        return NSScreen.mainScreen().frame()

    def _osx_available(self):
        '''What OSX reports as available frame for applications.'''
        from AppKit import NSScreen
        return NSScreen.mainScreen().visibleFrame()

    def __str__(self):
        return '%s,%s' % (self.origin, self.size)
