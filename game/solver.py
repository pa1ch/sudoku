from copy import deepcopy
from sys import exit
import sudoku as game


class Solver:
    @staticmethod
    def check_solve(sudoku):
        from game.correctnessChecker import CorrectnessChecker
        if sudoku.empty_cells_count == 0:
            if CorrectnessChecker.finally_check(sudoku):
                with open('solution.txt', 'r+', encoding='utf-8') as solution:
                    if sum(1 for line in solution) > game.args.solutions_count * (sudoku.dimension + 1) - 1:
                        exit()
                    for line in sudoku:
                        a = [str(i) for i in line]
                        solution.write(' '.join(a) + '\n')
                    solution.write('\n')
                sudoku.print_sudoku()
                print('Solution found!')
        else:
            len_shortest_set = sudoku.dimension + 1
            shortest_set_coordinates = None
            for line in range(sudoku.dimension):
                for column in range(sudoku.dimension):
                    if type(sudoku[line][column]) == set and len(sudoku[line][column]) < len_shortest_set:
                            shortest_set_coordinates = (line, column)
                            len_shortest_set = len(sudoku[line][column])
            Solver.try_choose_number(sudoku, shortest_set_coordinates[0], shortest_set_coordinates[1])

    @staticmethod
    def set_possible_numbers(sudoku, line, column, number_set):
        if type(sudoku[line][column]) == set:
            sudoku[line][column] = sudoku[line][column] & number_set
            Solver.find_exact_numbers(sudoku, line, column)

    @staticmethod
    def find_exact_numbers(sudoku, line, column):
        if len(sudoku[line][column]) == 1:
            sudoku[line][column] = sudoku[line][column].pop()
            sudoku.empty_cells_count -= 1
            for x in range(sudoku.dimension):
                Solver.discard_excess_numbers(sudoku, x, column, sudoku[line][column])
            for y in range(sudoku.dimension):
                Solver.discard_excess_numbers(sudoku, line, y, sudoku[line][column])
            Solver.discard_excess_numbers_for_squares(sudoku, line, column, sudoku[line][column])

    @staticmethod
    def discard_excess_numbers(sudoku, line, column, number):
        if type(sudoku[line][column]) == set and number in sudoku[line][column]:
            sudoku[line][column].discard(number)
            Solver.find_exact_numbers(sudoku, line, column)

    @staticmethod
    def discard_excess_numbers_for_squares(sudoku, line, column, number):
        for x in range(-(line % sudoku.squares_count), sudoku.squares_count - line % sudoku.squares_count):
            for y in range(-(column % sudoku.squares_count), sudoku.squares_count - column % sudoku.squares_count):
                if type(sudoku[line + x][column + y]) == set and number in sudoku[line + x][column + y]:
                    sudoku[line + x][column + y].discard(number)
                    Solver.find_exact_numbers(sudoku, line + x, column + y)

    @staticmethod
    def try_choose_number(sudoku, line, column):
        from game.correctnessChecker import CorrectnessChecker
        for number in sudoku[line][column]:
            new_sudoku = deepcopy(sudoku)
            new_sudoku[line][column] = number
            new_sudoku.empty_cells_count -= 1
            try:
                CorrectnessChecker.check_lines(new_sudoku, line)
                CorrectnessChecker.check_columns(new_sudoku, column)
                CorrectnessChecker.check_squares(new_sudoku, line, column, number)
                CorrectnessChecker.check_same_numbers_near(new_sudoku)
                Solver.check_solve(new_sudoku)
            except ValueError or TypeError:
                break


def main():
    pass


if __name__ == '__main__':
    main()
