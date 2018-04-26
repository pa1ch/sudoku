from math import sqrt


class CorrectnessChecker:
    @staticmethod
    def check_correctness(sudoku):
        if sudoku.dimension != len(sudoku._field):
            raise ValueError
        for y in range(sudoku.dimension):
            CorrectnessChecker.check_columns(sudoku, y)
        CorrectnessChecker.check_squares(sudoku)
        print('OK')

    @staticmethod
    def check_columns(sudoku, y):
        numbers = [i for i in range(1, sudoku.dimension + 1)]
        for x in range(sudoku.dimension):
            if sudoku[x][y] < 0 or sudoku[x][y] > sudoku.dimension:
                raise ValueError('Value must be > 0 and < '+str(sudoku.dimension + 1))
            if sudoku[x][y] == 0:
                continue
            elif numbers.count(sudoku[x][y]) == 1:
                numbers.remove(sudoku[x][y])
            else:
                raise ValueError('The numbers in the column must not be repeated')

    @staticmethod
    def check_line(line, dimension):
        if len(line) != dimension:
            raise ValueError('The length of the line must be equal to the dimension')
        numbers = [i for i in range(1, dimension + 1)]
        for item in line:
            if item < 0 or item > dimension:
                raise ValueError('Value must be > 0 and < '+str(dimension + 1))
            if item == 0:
                continue
            elif numbers.count(item) == 1:
                numbers.remove(item)
            else:
                raise ValueError('The numbers in the line must not be repeated')

    @staticmethod
    def check_squares(sudoku):
        squares_count = int(sqrt(sudoku.dimension))
        for x in range(squares_count, sudoku.dimension+1, squares_count):
            for y in range(squares_count, sudoku.dimension + 1, squares_count):
                CorrectnessChecker.check_nearest(sudoku, squares_count, x - 1, y - 1)

    @staticmethod
    def check_nearest(sudoku, square_count, x, y):
        numbers = [i for i in range(1, sudoku.dimension + 1)]
        for i in range(square_count):
            for j in range(square_count):
                if sudoku[x - i][y - j] < 0 or sudoku[x - i][y - j] > sudoku.dimension:
                    raise ValueError('Value must be > 0 and < ' + str(sudoku.dimension + 1))
                if sudoku[x - i][y - j] == 0:
                    continue
                elif numbers.count(sudoku[x - i][y - j]) == 1:
                    numbers.remove(sudoku[x - i][y - j])
                else:
                    raise ValueError('The numbers in the square must not be repeated')


def main():
    pass


if __name__ == '__main__':
    main()
