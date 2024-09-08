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
        self.assertEquals(result, 3)
    
    def test_muiltiple_numbers(self):
        result = Add("1,2,3")
        self.assertEquals(result, 6)

    def test_newline_input(self):
        result = Add("1\n2,3")
        self.assertEquals(result, 6)
    
    def test_dynamic_delimiter(self):
        result = Add("//;\n1;2;3")
        self.assertEquals(result, 6)

        result = Add("//;*\n1;*2;*3")
        self.assertEquals(result, 6)
    
    def test_non_numerical_inputs(self):
        test_inputs = ("a", "1,a,2")
        
        for input_value in test_inputs:
            with self.assertRaises(ValueError) as e:
                result = Add(input_value)
            
            self.assertEqual(str(e.exception), "Non-numerical input received")
    
    
        
