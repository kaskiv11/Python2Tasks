import unittest
from operations import *


class TestMAthOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 15), 25)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_raises(self):
        with self.assertRaises(TypeError):
            subtract("10", 5)

    def test_is_even(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(9))

    def test_found_item(self):
        numbers = ["Hello", 8, "Buy"]
        number = 8
        self.assertTrue(found_item(numbers, number))
