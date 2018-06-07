#! --shebang

from yourapplication.sudoku_solver.driver import sudoku_solver
from yourapplication.Eight_Puzzle.driver import eight_puzzle_ast
from flask import Flask 
from flask import url_for
from flask import render_template
from flask import request
from flask import make_response
from flask import jsonify
from flask import json

app = Flask(__name__) 

@app.route('/')
@app.route('/Resume')
def getResumePage():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        sudoku_unsolved = request.form['sudoku_board']
        sudoku_solved, sudoku_method = sudoku_solver(sudoku_unsolved)
        return (sudoku_solved)

@app.route('/Projects')
def getProjectsPage():
    return render_template('index_projects.html')

@app.route('/Projects/GoogleMap')
def getGoogleMapsPage():
    return render_template('index_projects_googlemap.html')

@app.route('/Projects/Sudoku_Solver', methods=['POST', 'GET'])
def getSudokuPage():
    if request.method == 'GET':
        return render_template('index_projects_sudokusolver.html')
    if request.method == 'POST':
        sudoku_unsolved = request.form['sudoku_board']
        sudoku_solved, sudoku_method = sudoku_solver(sudoku_unsolved)
        return (sudoku_solved)

@app.route('/Projects/Eight_Puzzle_Solver', methods=['POST', 'GET'])
def getEightPuzzlePage():
    if request.method == 'GET':
        return render_template('index_projects_eightpuzzlesolver.html')
    if request.method == 'POST':
        eight_puzzle_unsolved = request.form['eight_puzzle_board']
        true_path, cost, n_nodes, level, search_depth, completion_time, memory = eight_puzzle_ast(eight_puzzle_unsolved)
        solved_board = ''
        for x in true_path:
            solved_board += x
            solved_board += ', '
        return (solved_board)

@app.route('/Skills')
def getSkillsPage():
    return ("/nUNDER CONSTRUCTION!!/n/nThis will be my skills page")

@app.route('/About_me')
def getAboutMePage():
    return ('/nUNDER CONSTRUCTION!!/n/nThis will be my "About me" page')

@app.route('/Contact_me')
def getContactMePage():
    return ('/nUNDER CONSTRUCTION!!/n/nThis will be my "Contact Me" page')

@app.route('/testing')
def tester():
    return render_template('test.html')

@app.route('/testing/sudoku/<board>', methods=['GET','POST'])
def tester_sudoku(board):
    if request.method == 'GET':
        resp = {'abc':'Some Message!'}
        return jsonify(resp)
    if request.method == 'POST':

        sudoku_unsolved = board
        print ('\n\n::::New Print Line:::::')
        print (board)

        sudoku_solved, sudoku_method = sudoku_solver(sudoku_unsolved)
        resp = {'solution' : sudoku_solved}
        return jsonify(resp)
    
@app.route('/testing/react')
def tester_react():
    return render_template('test_react.html')

if __name__ == '__main__':
    app.run()
