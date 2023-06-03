import unittest
from lisp import *
from helper_functions import *


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

    def test_add(self):
        self.assertEqual(add([1, 2, 3]), 6)
        self.assertEqual(add([5, -2, 8]), 11)
        self.assertEqual(add([-10, 20, 30]), 40)

    def test_equals(self):
        self.assertTrue(equals([5, 5]), True)


    def test_car(self):
        self.assertEqual(car([['a', 'b'], ['c', 'd']]), 'a')
        self.assertEqual(car(['quote', 'hello']), 'h')
        self.assertEqual(car(['quote', ['x', 'y', 'z']]), 'x')

    def test_cdr(self):
        self.assertEqual(cdr([['a', 'b'], ['c', 'd']]), ['b'])
        self.assertEqual(cdr(['quote', 'hello']), 'ello')
        self.assertEqual(cdr(['quote', ['x', 'y', 'z']]), ['y', 'z'])

    def test_subtract(self):
        self.assertEqual(subtract([10, 5, 3]), 2)
        self.assertEqual(subtract([7, -2, 4]), 5)
        self.assertEqual(subtract([-10, 5, 2]), -17)

    def test_divide(self):
        self.assertEqual(divide([10, 2, 2]), 2.5)
        self.assertEqual(divide([20, -5, 2]), -2)
        self.assertEqual(divide([100, 5, 4]), 5)

    def test_multiply(self):
        self.assertEqual(multiply([2, 3, 4]), 24)
        self.assertEqual(multiply([-1, 5, 2]), -10)
        self.assertEqual(multiply([10, 5, 0]), 0)

    def test_is_atom(self):
        pass


    def test_quote(self):
        self.assertEqual(quote(['quote', 'hello']), 'hello')
        self.assertEqual(quote(['quote', [1, 2, 3]]), [1, 2, 3])
        self.assertEqual(quote(['quote', 5]), 5)
       

    def test_cons(self):
        pass
   

    def test_cond(self):
        pass



if __name__ == '__main__':
    unittest.main()
