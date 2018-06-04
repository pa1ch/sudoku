from game.correctnessChecker import *
from math import sqrt
import argparse


def is_square(n):
    return sqrt(n).is_integer()


class Sudoku:
    def __init__(self, file_name):
        self._field = []
        self.empty_cells_count = 0
        try:
            with open(file_name, encoding='utf-8') as file:
                self.dimension = int(file.readline())
                self.squares_count = int(sqrt(self.dimension))
                if not is_square(self.dimension):
                    raise ValueError('Dimension must be a perfect square')
                for line in file:
                    self.append([int(item) for item in line.split()])
            CorrectnessChecker.check_correctness(self)
        except FileNotFoundError:
            raise FileNotFoundError('Sorry. File not found :( , but you can '
                                    'create file "gameField.txt" in the root'
                                    ' directory and also fill it in '
                                    'accordance with the format described '
                                    'in the README.')
        if self.dimension != len(self._field):
            raise ValueError
        open("solution.txt", "w").close()

    def __getitem__(self, x):
        return self._field[x]

    def __setitem__(self, x, value):
        self._field[x] = value

    def append(self, line):
        if len(line) == 0:
            return
        CorrectnessChecker.check_input(self, line)
        self._field.append(line)

    def print_sudoku(self):
        for line in self._field:
            print(line)


def main():
    file = args.filename
    sudoku = Sudoku(file)
    try:
        CorrectnessChecker.check_same_numbers_near(sudoku)
    except ValueError:
        print('The original file did not meet the additional requirements. '
              'Solution found without regard to additional requirements')
    Solver.check_solve(sudoku)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',  nargs='?', default='gameField.txt')
    parser.add_argument('solutions_count', type=int, nargs='?', default=5)
    args = parser.parse_args()
    return args


args = create_parser()


if __name__ == '__main__':
    main()
