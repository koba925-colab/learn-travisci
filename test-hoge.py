#! /usr/bin/env python3

import unittest
from hoge import hogehoge, pogepoge


class TestHoge(unittest.TestCase):
    def test_hogehoge(self):
        self.assertEqual(hogehoge(2, 5), 7)
        self.assertEqual(hogehoge(5, 2), 3)

    def test_pogepoge(self):
        self.assertEqual(pogepoge(3), 6)


if __name__ == "__main__":
    unittest.main()
