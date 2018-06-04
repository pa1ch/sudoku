from game.solver import Solver
from copy import copy


class CorrectnessChecker:
    @staticmethod
    def check_correctness(sudoku):
        for y in range(sudoku.dimension):
            CorrectnessChecker.check_columns(sudoku, y)
        CorrectnessChecker.check_squares(sudoku)

    @staticmethod
    def check_lines(sudoku, line):
        numbers = {i for i in range(1, sudoku.dimension + 1)}
        for column in range(sudoku.dimension):
            if type(sudoku[line][column]) == set:
                continue
            elif sudoku[line][column] in numbers:
                numbers.discard(sudoku[line][column])
            else:
                raise ValueError('The numbers must not be repeated. Line "'
                                 + str(line) + '" is not correct')
        for column in range(sudoku.dimension):
            Solver.set_possible_numbers(sudoku, line, column, numbers)

    @staticmethod
    def check_columns(sudoku, column):
        numbers = {i for i in range(1, sudoku.dimension + 1)}
        for line in range(sudoku.dimension):
            if type(sudoku[line][column]) == set:
                continue
            elif sudoku[line][column] in numbers:
                numbers.discard(sudoku[line][column])
            else:
                raise ValueError('The numbers must not be repeated. '
                                 'Column ' + str(column) + ' is not correct')
        for line in range(sudoku.dimension):
            Solver.set_possible_numbers(sudoku, line, column, numbers)

    @staticmethod
    def check_input(sudoku, line):
        if len(line) != sudoku.dimension:
            raise ValueError('The length of the line must be equal '
                             'to the dimension')
        numbers = {i for i in range(1, sudoku.dimension + 1)}
        for item in range(sudoku.dimension):
            if line[item] < 0 or line[item] > sudoku.dimension:
                raise ValueError('Value must be > 0 and < '
                                 + str(sudoku.dimension + 1))
            if line[item] == 0:
                continue
            elif line[item] in numbers:
                numbers.discard(line[item])
            else:
                raise ValueError('The numbers must not be repeated. Line "'
                                 + str(line) + '" is not correct')
        for item in range(sudoku.dimension):
            if line[item] == 0:
                line[item] = copy(numbers)
                sudoku.empty_cells_count += 1

    @staticmethod
    def check_squares(sudoku, line=None, column=None, number=None):
        if line is not None and column is not None and number is not None:
            Solver.discard_excess_numbers_for_squares(sudoku, line, column, number)
            return
        for x in range(sudoku.squares_count, sudoku.dimension + 1, sudoku.squares_count):
            for y in range(sudoku.squares_count, sudoku.dimension + 1, sudoku.squares_count):
                CorrectnessChecker.check_nearest(sudoku, x - 1, y - 1)

    @staticmethod
    def check_nearest(sudoku, x, y):
        numbers = {i for i in range(1, sudoku.dimension + 1)}
        for i in range(sudoku.squares_count):
            for j in range(sudoku.squares_count):
                if type(sudoku[x - i][y - j]) == set:
                    continue
                elif sudoku[x - i][y - j] in numbers:
                    numbers.discard(sudoku[x - i][y - j])
                else:
                    raise ValueError('The numbers in the square must not '
                                     'be repeated')
        for i in range(sudoku.squares_count):
            for j in range(sudoku.squares_count):
                Solver.set_possible_numbers(sudoku, x - i, y - j, numbers)

    @staticmethod
    def check_same_numbers_near(sudoku):
        for x in range(sudoku.squares_count - 1, sudoku.dimension - sudoku.squares_count, sudoku.squares_count):
            for y in range(sudoku.squares_count - 1, sudoku.dimension - sudoku.squares_count, sudoku.squares_count):
                if (type(sudoku[x][y]) != set and sudoku[x][y] != 0 and type(sudoku[x+1][y+1]) != set and
                        sudoku[x+1][y+1] != 0 and sudoku[x][y] == sudoku[x+1][y+1]):
                    raise ValueError('The numbers in the mini-square must not be repeated')
                if (type(sudoku[x+1][y]) != set and sudoku[x+1][y] != 0 and type(sudoku[x][y+1]) != set and
                        sudoku[x][y+1] != 0 and sudoku[x+1][y] == sudoku[x][y+1]):
                    raise ValueError('The numbers in the mini-square must not be repeated')

    @staticmethod
    def finally_check(sudoku):
        try:
            for i in range(sudoku.dimension):
                CorrectnessChecker.check_lines(sudoku, i)
                CorrectnessChecker.check_columns(sudoku, i)
            CorrectnessChecker.check_squares(sudoku)
            CorrectnessChecker.check_same_numbers_near(sudoku)
        except ValueError or TypeError:
            return False
        else:
            return True


def main():
    pass


if __name__ == '__main__':
    main()
