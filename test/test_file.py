import unittest


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'File not found'



class TestFileReading(unittest.TestCase):

    def test_read_existing_file(self):
        content = read_file('file.txt')
        self.assertIsInstance(content, str)

    def test_read_non_existing_file(self):
        fake_file = "fake_file.txt"
        content = read_file(fake_file)
        self.assertEqual(content, "File not found")

