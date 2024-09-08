import unittest

from calculator import Add, comma_separator


class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        result = Add("")
        self.assertEqual(result, 0)
    
    def test_one_number(self):
        result = Add("1")
        self.assertEqual(result, 1)

    def test_two_numbers(self):
        result = Add("1,2")
        self.assertEqual(result, 3)
    
    def test_muiltiple_numbers(self):
        result = Add("1,2,3")
        self.assertEqual(result, 6)

    def test_newline_input(self):
        result = Add("1\n2,3")
        self.assertEqual(result, 6)
    
    def test_dynamic_delimiter(self):
        result = Add("//;\n1;2;3")
        self.assertEqual(result, 6)

        result = Add("//;*\n1;*2;*3")
        self.assertEqual(result, 6)
    
    def test_negative_numbers(self):
        with self.assertRaises(Exception) as e:
            result = Add(f"1,2,-3,-4")

        self.assertEqual(str(e.exception), f"negative numbers not allowed -3,-4")
