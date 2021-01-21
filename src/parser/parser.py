import itertools


class Parser:

    def __init__(self):
        pass

    def __del__(self):
        pass

    zero_digit_list = [
        ' _ ',
        '| |',
        '|_|'
    ]

    one_digit_list = [
        '   ',
        '  |',
        '  |'
    ]

    two_digit_list = [
        ' _ ',
        ' _|',
        '|_ '
    ]

    three_digit_list = [
        ' _ ',
        ' _|',
        ' _|'
    ]

    four_digit_list = [
        '   ',
        '|_|',
        '  |'
    ]

    five_digit_list = [
        ' _ ',
        '|_ ',
        ' _|'
    ]

    six_digit_list = [
        ' _ ',
        '|_ ',
        '|_|'
    ]

    seven_digit_list = [
        ' _ ',
        '  |',
        '  |'
    ]

    eight_digit_list = [
        ' _ ',
        '|_|',
        '|_|'
    ]

    nine_digit_list = [
        ' _ ',
        '|_|',
        ' _|'
    ]

    def zero_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.zero_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def one_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.one_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def two_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.two_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def three_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.three_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def four_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.four_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def five_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.five_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def six_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.six_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def seven_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.seven_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def eight_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.eight_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    def nine_difference(self, digit_list):
        counter = 0
        for n in range(len(digit_list)):
            for m in range(len(digit_list[0])):
                if self.nine_digit_list[n][m] != digit_list[n][m]:
                    counter += 1
        return counter

    check_number_difference = {
        0: zero_difference,
        1: one_difference,
        2: two_difference,
        3: three_difference,
        4: four_difference,
        5: five_difference,
        6: six_difference,
        7: seven_difference,
        8: eight_difference,
        9: nine_difference,
    }

    AMB = 'AMB'
    ILL = 'ILL'
    ERR = 'ERR'

    def parse(self, scanned_text, validate_checksum_iterative=True, guess_possible_number=False, number_of_different_characters=1.0):
        array_of_chars = list()
        lines = scanned_text.split('\n')
        for line in lines:
            array_of_chars.append(list(line))

        output = []
        output_with_question_mark = []
        for digit_number in range(1, 10):
            # print(self.get_one_digit_list(array_of_chars, digit_number))
            one_digit_list = self.get_one_digit_list(array_of_chars, digit_number)
            digit, possible_digits = self.recognize_digit(one_digit_list, guess_possible_number=guess_possible_number, number_of_different_characters=number_of_different_characters)
            if not guess_possible_number:
                output.append(digit)
            else:
                if digit != '?':
                    possible_digits.insert(0, int(digit))
                output.append(possible_digits)
                output_with_question_mark.append(digit)

        illegal, valid_checksums = self.validate_checksum(output, guess_possible_number, validate_checksum_iterative)
        if not guess_possible_number:
            if len(valid_checksums) == 1:
                return ''.join(output)
            else:
                if illegal:
                    return ' '.join((''.join(output), self.ILL))
                else:
                    return ' '.join((''.join(output), self.ERR))
        else:
            if len(valid_checksums) == 0:
                return ' '.join((''.join(output_with_question_mark), self.ILL))
            elif len(valid_checksums) == 1:
                return ''.join(output_with_question_mark)
            elif len(valid_checksums) > 1:
                return ''.join(output_with_question_mark) + ' AMB [' + ', '.join('\'' + str(''.join(str(element) for element in valid_checksum) + '\'') for valid_checksum in valid_checksums) + ']'

    def get_one_digit_list(self, array_of_chars, digit_number):
        return [array_of_chars[i][3*digit_number-3:3*digit_number] for i in range(3)]

    def pad_or_truncate(self, digit_list, target_length):
        return digit_list[:target_length] + [' '] * (target_length - len(digit_list))

    def recognize_digit(self, digit_list, guess_possible_number=False, number_of_different_characters=1.0):
        digit_list = self.normalize_digit(digit_list)
        digit = '?'
        possible_digit = []
        for i in range(0, 10):
            difference = self.check_number_difference[i](self, digit_list)
            if guess_possible_number:
                if difference == 0.0:
                    digit = str(i)
                elif difference <= number_of_different_characters:
                    possible_digit.append(i)
            else:
                if difference == 0.0:
                    digit = str(i)
        return digit, possible_digit

    def validate_checksum(self, output, guess_possible_number=False, validate_checksum_iterative=True):
        checksum = 0
        illegal = False
        valid_checksums = []
        if not guess_possible_number:
            for i in range(8, -1, -1):
                if isinstance(output[i], int) or output[i].isdigit():
                    checksum += ((9 - i) * int(output[i]))
                else:
                    illegal = True
            if checksum % 11 == 0:
                valid_checksums.append(''.join(str(out) for out in output))
        else:
            if validate_checksum_iterative:
                valid_checksums = self.calculate_valid_checksums_iterate(output)
            else:
                valid_checksums = self.calculate_valid_checksums_recursive(output)

        return illegal, valid_checksums

    def calculate_valid_checksums_recursive(self, output):
        valid_checksums = []
        for i in range(len(output)):
            if isinstance(output[i], int):
                if i == len(output) - 1:
                    illegal, valid_checksum = self.validate_checksum(output)
                    valid_checksums.extend(valid_checksum)
                    return valid_checksums
            else:
                for j in range(len(output[i])):
                    next = output[0:i]
                    next.append(output[i][j])
                    next.extend(output[i+1:])
                    temp_valid_checksums = self.calculate_valid_checksums_recursive(next)
                    if temp_valid_checksums is not None:
                        valid_checksums.extend(temp_valid_checksums)
                return valid_checksums

    def calculate_valid_checksums_iterate(self, output):
        valid_checksums = []
        all_combination = list(itertools.product(*output))
        for combination in all_combination:
            checksum = 0
            for j in range(len(combination)):
                checksum += (j+1) * int(combination[len(combination) - j - 1])
            if checksum % 11 == 0:
                valid_checksums.append(combination)
        return valid_checksums

    def normalize_digit(self, digit_list):
        digit_list[0] = self.pad_or_truncate(digit_list[0], 3)
        digit_list[1] = self.pad_or_truncate(digit_list[1], 3)
        digit_list[2] = self.pad_or_truncate(digit_list[2], 3)
        digit_list[0] = ''.join(digit_list[0])
        digit_list[1] = ''.join(digit_list[1])
        digit_list[2] = ''.join(digit_list[2])
        return digit_list


