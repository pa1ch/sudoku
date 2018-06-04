import unittest
from sudoku import Sudoku
from game.correctnessChecker import CorrectnessChecker


class SudokuTests(unittest.TestCase):
    def test_bad_sudoku(self):
        with self.assertRaises(ValueError):
            Sudoku('tests/badTestField.txt')

    def test_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            Sudoku('tests/randomTestField.txt')

    def test_bad_dimension(self):
        with self.assertRaises(ValueError):
            Sudoku('tests/badDimensionTestField.txt')

    def test_bad_format_sudoku(self):
        with self.assertRaises(ValueError):
            Sudoku('tests/badTestField.txt')


class CheckerTests(unittest.TestCase):
    def setUp(self):
        self.bad_sudoku = Sudoku('tests/goodTestSolution.txt')
        self.bad_sudoku[0][0] = 7
        self.bad_sudoku[3][3] = 15
        del(self.bad_sudoku[4][4])
        self.bad_sudoku[5][5] = 'M'
        self.bad_sudoku[6][2] = 8

    def test_bad_line(self):
        with self.assertRaises(ValueError):
            CorrectnessChecker.check_lines(self.bad_sudoku, 0)

    def test_bad_column(self):
        with self.assertRaises(ValueError):
            CorrectnessChecker.check_columns(self.bad_sudoku, 0)

    def test_bad_square(self):
        with self.assertRaises(ValueError):
            CorrectnessChecker.check_nearest(self.bad_sudoku, 2, 2)

    def test_bad_number_in_line(self):
        with self.assertRaises(ValueError):
            CorrectnessChecker.check_input(self.bad_sudoku, self.bad_sudoku[3])

    def test_bad_line_dimension(self):
        with self.assertRaises(ValueError):
            CorrectnessChecker.check_input(self.bad_sudoku, self.bad_sudoku[4])

    def test_letter_in_line(self):
        with self.assertRaises(TypeError):
            CorrectnessChecker.check_input(self.bad_sudoku, self.bad_sudoku[5])

    def test_good_solution(self):
        self.assertTrue(CorrectnessChecker.finally_check(Sudoku('tests/goodTestSolution.txt')))

    def test_same_numbers_near(self):
        with self.assertRaises(ValueError):
            CorrectnessChecker.check_same_numbers_near(self.bad_sudoku)


if __name__ == '__main__':
    unittest.main()
