import unittest
from src.math import Math

class MathTest(unittest.TestCase):
    def test_add_integers(self):
        #To make test fail
        self.assertEqual(Math.add_integers(2,9), 11)
