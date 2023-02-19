import unittest
from main import multiply


class TestSimple(unittest.TestCase):

    def test_multiply(self):
        assert multiply(2, 4) == 8

    def test_multiply2(self):
        self.assertEqual(multiply(2, 5), 10)
