import unittest

from calculator import Add

class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        result = Add("")
        self.assertEquals(result, 0)
    
    def test_one_number(self):
        result = Add("1")
        self.assertEquals(result, 1)

    def test_two_numbers(self):
        result = Add("1,2")
        self.assertEquals(result, 1)
