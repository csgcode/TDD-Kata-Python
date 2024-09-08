import unittest

from calculator import Add

class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        result = Add("")
        self.assertEquals(result, 0)