import unittest

from src.parser.parser import Parser


class ParserTests(unittest.TestCase):
    TEST_FILE = '../data/test_data'

    def setUp(self):
        self.parser = Parser()

    def tearDown(self):
        parser = None

    def test_iterative(self):
        i = 0
        with open(self.TEST_FILE, 'r') as fp:
            while True:
                try:
                    value = next(fp) + next(fp) + next(fp)
                    value = value[:-1]
                    next(fp)
                    expected = next(fp)[3:-1]
                    if i <= 13:
                        actual = self.parser.parse(value, validate_checksum_iterative=True, guess_possible_number=False)
                    else:
                        actual = self.parser.parse(value, validate_checksum_iterative=True, guess_possible_number=True)
                    if expected == actual:
                        print(expected + ' == ' + actual)
                    else:
                        print(expected + ' != ' + actual)
                    i += 1
                    # self.assertEqual(expected, actual)
                except StopIteration:
                    break

    def test_recursive(self):
        i = 0
        with open(self.TEST_FILE, 'r') as fp:
            while True:
                try:
                    value = next(fp) + next(fp) + next(fp)
                    value = value[:-1]
                    next(fp)
                    expected = next(fp)[3:-1]
                    if i <= 13:
                        actual = self.parser.parse(value, validate_checksum_iterative=False, guess_possible_number=False)
                    else:
                        actual = self.parser.parse(value, validate_checksum_iterative=False, guess_possible_number=True)
                    if expected == actual:
                        print(expected + ' == ' + actual)
                    else:
                        print(expected + ' != ' + actual)
                    i += 1
                    # self.assertEqual(expected, actual)
                except StopIteration:
                    break


if __name__ == '__main__':
    unittest.main()
