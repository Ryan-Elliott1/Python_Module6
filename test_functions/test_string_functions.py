import unittest
from more_functions import string_functions


class FunctionTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(string_functions.multiply_string("ryan", 3), "ryanryanryan")
