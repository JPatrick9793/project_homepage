## SUDOKU SOLVER
This Folder contains the sudoku solver python file.
Use as follows:

> from sudoku_solver.driver import sudoku_solver
> 
> answ, meth = sudoku_solver( **BOARD** )

where **BOARD** is a string defining the incomplete sudoku board (with Zero's representing the blank spaces)

* answ = string containing solved board
* meth = either 'AC3' or 'BTS' depending on which was used to solve
