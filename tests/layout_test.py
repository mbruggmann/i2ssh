import unittest
from i2ssh.layout import Layout

class LayoutTest(unittest.TestCase):

    def test_fromspec(self):
        config = {'layout': '2x3'}
        l = Layout(config)
        self.assertEqual(2, l.cols)
        self.assertEqual(3, l.rows)

    def test_nrhosts(self):
        self.assertEqual((1, 1), self._for_nr_hosts(0))
        self.assertEqual((1, 1), self._for_nr_hosts(1))
        self.assertEqual((2, 1), self._for_nr_hosts(2))
        self.assertEqual((2, 1), self._for_nr_hosts(3))
        self.assertEqual((2, 2), self._for_nr_hosts(4))
        self.assertEqual((3, 2), self._for_nr_hosts(5))
        self.assertEqual((4, 4), self._for_nr_hosts(16))
        self.assertEqual((5, 4), self._for_nr_hosts(17))


    def _for_nr_hosts(self, nr_hosts):
        config = {'hosts': ['' for i in range(0, nr_hosts)]}
        l = Layout(config)
        return (l.cols, l.rows)
