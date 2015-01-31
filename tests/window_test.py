import unittest
from mock import patch
from i2ssh.window import Point, Size, Window

class WindowTest(unittest.TestCase):

    def test_fromconfig(self):
        config = {'window': '0, 10, 100, 300'}
        w = Window(config)
        self.assertEqual(0, w.origin.x)
        self.assertEqual(10, w.origin.y)
        self.assertEqual(100, w.size.width)
        self.assertEqual(300, w.size.height)

    def test_maximize(self):
        origin = Point(x=0, y=37)
        size = Size(width=1440, height=840)
        with patch.object(Window, '_available_frame', return_value=(origin, size)):
            w = Window({})
            self.assertEquals(origin, w.origin)
            self.assertEquals(size, w.size)
