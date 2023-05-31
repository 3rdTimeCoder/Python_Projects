import unittest
from io import StringIO
import sys
from lisp_intepreter import *


class MyTestCase(unittest.TestCase):

    def test_tokenize(self):
        tokens = tokenize("(eq 2 3)")
        self.assertEqual([ "(", "eq", "2", "3", ")"], tokens)

    
    def test_parenthesis_correct(self):
        self.assertTrue(parenthesis_correct("(eq 2 3)"))
        self.assertFalse(parenthesis_correct("(atom '(- 2 3)"))

    
    def test_valid_token(self):
        self.assertTrue(tokens_valid([ "(", "eq", "2", "3", ")"]))
        self.assertFalse(tokens_valid([ "(", "+", "2", "3", ")", ";"]))




if __name__ == '__main__':
    unittest.main()
