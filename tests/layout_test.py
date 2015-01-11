import unittest
from i2ssh.layout import Layout

class LayoutTest(unittest.TestCase):

    def test_fromspec(self):
        config = {'hosts': 5*[''], 'layout': '2x3'}
        l = Layout(config)
        self.assertEqual(2, l.cols)
        self.assertEqual(3, l.rows)
        self.assertEqual(1, l.disabled)

    def test_nrhosts_zero(self):
        self.assertEqual((1, 1, 1), self._for_nr_hosts(0))

    def test_nrhosts_one(self):
        self.assertEqual((1, 1, 0), self._for_nr_hosts(1))

    def test_nrhosts_exact_squares(self):
        self.assertEqual((2, 2, 0), self._for_nr_hosts(4))
        self.assertEqual((3, 3, 0), self._for_nr_hosts(9))
        self.assertEqual((4, 4, 0), self._for_nr_hosts(16))

    def test_nrhosts_exact_nonsquares(self):
        self.assertEqual((2, 1, 0), self._for_nr_hosts(2))
        self.assertEqual((3, 2, 0), self._for_nr_hosts(6))
        self.assertEqual((4, 3, 0), self._for_nr_hosts(12))

    def test_nrhosts_with_remainders(self):
        self.assertEqual((2, 2, 1), self._for_nr_hosts(3))
        self.assertEqual((3, 2, 1), self._for_nr_hosts(5))
        self.assertEqual((3, 3, 2), self._for_nr_hosts(7))
        self.assertEqual((4, 3, 2), self._for_nr_hosts(10))
        self.assertEqual((4, 4, 3), self._for_nr_hosts(13))
        self.assertEqual((5, 4, 3), self._for_nr_hosts(17))

    def _for_nr_hosts(self, nr_hosts):
        config = {'hosts': nr_hosts*['']}
        l = Layout(config)
        return (l.cols, l.rows, l.disabled)
