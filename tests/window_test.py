import unittest
from mock import patch
from i2ssh.window import Point, Size, Window

class MockFrame:
     def __init__(self, x, y, w, h):
         self.origin = Point(x, y)
         self.size = Size(w, h)

class WindowTest(unittest.TestCase):

    def test_fromconfig(self):
        config = {'window': '0, 10, 100, 300'}
        w = Window(config)
        self.assertEqual(0, w.origin.x)
        self.assertEqual(10, w.origin.y)
        self.assertEqual(100, w.size.width)
        self.assertEqual(300, w.size.height)

    def test_default(self):
        frame = MockFrame(0, 0, 1440, 900)
        available = MockFrame(0, 37, 1440, 840)

        with patch.object(Window, '_osx_frame', return_value=frame):
            with patch.object(Window, '_osx_available', return_value=available):
                w = Window({})
                self.assertEquals(0, w.origin.x)
                self.assertEquals(23, w.origin.y)
                self.assertEquals(1440, w.size.width)
                self.assertEquals(840, w.size.height)
