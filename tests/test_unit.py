import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
NO_PATH = sys.maxsize


# Import Floyd Warshall recursive function
from floyd.floyd_rec import Floyd
from test_cases import (input_a, output_a)


 # Testing the Floyd function
class FloydTestFunc(unittest.TestCase):

# Task-specific method   
# Equal to check if the output Floyd function gives is expectated
    
    def test_Floyd(self):
        self.assertEqual(Floyd(input_a), input_a)
        print("Success! Inputs are correct.")
    def test_Floyd_a(self):
        self.assertEqual(Floyd(input_a), output_a, "Failed! Inputs are Incorrect.")

#  Production check
# Using asserRaises to check if Floyd functiotn handles classes/type of inputs    
    def test_Floyd_b(self):
        self.assertRaises(TypeError, Floyd, True)
    
    
if __name__ == '__main__':
    unittest.main()






