from game.correctnessChecker import *


def is_square(n):
    return sqrt(n).is_integer()


class Sudoku:
    def __init__(self, file_name):
        self._field = []
        try:
            with open(file_name, encoding='utf-8') as file:
                self.dimension = int(file.readline())
                if not is_square(self.dimension):
                    raise ValueError('Dimension must be a perfect square')
                for line in file:
                    self.append([int(item) for item in line.split()], self.dimension)
        except FileNotFoundError:
            print('File not found.')
        except ValueError:
            print('Invalid file format.')

    def __getitem__(self, x):
        return self._field[x]

    def __setitem__(self, x, value):
        self._field[x] = value

    def append(self, x, y, digit):
        try:
            digit = int(digit)
        except ValueError:
            print('Value must be integer')
            digit = 0
        if x < 1 or x > 9 or y < 1 or y > 9 or digit < 0 or digit > 9:
            raise ValueError
        self[x - 1][y - 1] = digit

    def append(self, line, dim):
        if len(line) == 0:
            return
        try:
            CorrectnessChecker.check_line(line, dim)
        except ValueError:
            raise ValueError('line "'+str(line)+'" is not correct')
        self._field.append(line)

    def print_sudoku(self):
        for line in self._field:
            print(line)


def main():
    sudoku = Sudoku('gameField.txt')
    sudoku.print_sudoku()
    CorrectnessChecker.check_correctness(sudoku)


if __name__ == '__main__':
    main()
