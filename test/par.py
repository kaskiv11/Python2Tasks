import unittest


def is_even(n):
    return n % 2 == 0


class TestIEven(unittest.TestCase):
    def test_is_even(self):
        test_case = [2, 3, 10, 11, 100, 101]
        results = [True, False, True, False, True, False]

        for number, result in zip(test_case, results):
            with self.subTest(number=number):
                self.assertEqual(is_even(number), result)

