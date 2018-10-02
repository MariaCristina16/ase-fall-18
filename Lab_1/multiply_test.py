import calculator as c
import unittest
 
class TestMultiply(unittest.TestCase):
 
    def test_multiply_integers_positive(self):
        result = c.multiply(1, 2)
        self.assertEqual(result, 2)

    def test_multiply_integers_negative(self):
        result = c.multiply(-1, -2)
        self.assertEqual(result, 2)    

    def test_multiply_integers_pos_neg(self):
        result = c.multiply(1, -2)
        self.assertEqual(result, -2)  

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(-1, 2)
        self.assertEqual(result, -2)  
 
    def test_multiply_integers_neg_pos(self):
        result = c.multiply(0, 2)
        self.assertEqual(result, 0)  

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(2, 0)
        self.assertEqual(result, 0)  

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(-2, 0)
        self.assertEqual(result, 0)  

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(0, -2)
        self.assertEqual(result, 0)  
 
if __name__ == '__main__':
    unittest.main()