Sudoku solver by Chugaev Pavel aka A57RO
chugaev1998@gmail.com
t.me/a57r0

1. Write your Sudoku in a file 'gameField.txt' in the format:
~~~
dimension of Sudoku

<Sudoku>
~~~

The numbers should be written sequentially separated by a space.
Write each line of Sudoku with a new line in file.

For example:
~~~
9

5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3       <-- it is a valid format of 'gameField.txt'
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
~~~

2. Run 'solver.py' program with 2 arguments:
    -[file name (if the file is in the same directory as the project) or path to file] (by default gameField.txt)
    -[number of solutions to be found] (by default 5)

3. Your Sudoku solutions will be available in a file 'solution.txt'

4. ???

5. PROFIT!