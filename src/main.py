from src.parser.parser import Parser


class BankOCR:
    TEST_FILE = '../data/test_data'

    def __init__(self):
        self.parser = Parser()
        pass

    def __del__(self):
        parser = None
        pass

    def run_test(self, iterative=True):
        i = 0
        with open(self.TEST_FILE, 'r') as fp:
            while True:
                try:
                    value = next(fp) + next(fp) + next(fp)
                    value = value[:-1]
                    next(fp)
                    expected = next(fp)[3:-1]

                    if i <= 13:
                        actual = self.parser.parse(value, validate_checksum_iterative=iterative, guess_possible_number=False)
                    else:
                        actual = self.parser.parse(value, validate_checksum_iterative=iterative, guess_possible_number=True)
                    if expected == actual:
                        print(expected + ' == ' + actual)
                    else:
                        print(expected + ' != ' + actual)
                    i += 1
                except StopIteration:
                    break

    def main(self):
        self.run_test(iterative=True)
        self.run_test(iterative=False)


if __name__ == '__main__':
    bank_ocr = BankOCR()
    bank_ocr.main()

