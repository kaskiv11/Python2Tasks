import unittest


class TestExample(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]

    def tearDown(self):
        self.data = None

    def test_sum(self):
        result = sum(self.data)
        self.assertEqual(result, 15)

    def test_contains(self):
        self.assertIn(3, self.data)

