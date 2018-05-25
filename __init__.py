#! --shebang

from yourapplication.sudoku_solver.driver import sudoku_solver
from flask import Flask 
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__) 

@app.route('/', methods=['POST', 'GET']) 
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        sudoku_unsolved = request.form['sudoku_board']
        sudoku_solved, sudoku_method = sudoku_solver(sudoku_unsolved)
        return (sudoku_solved)
        # return (sudoku_unsolved)
        
    
@app.route('/Resume')
def getResumePage():
    return ("/nUNDER CONSTRUCTION!!/n/nThis will be my resume page")

@app.route('/Projects')
def getProjectsPage():
    return render_template('index_projects')

@app.route('/Skills')
def getSkillsPage():
    return ("/nUNDER CONSTRUCTION!!/n/nThis will be my skills page")

@app.route('/About_me')
def getAboutMePage():
    return ('/nUNDER CONSTRUCTION!!/n/nThis will be my "About me" page')

@app.route('/Contact_me')
def getContactMePage():
    return ('/nUNDER CONSTRUCTION!!/n/nThis will be my "Contact Me" page')

if __name__ == '__main__':
    app.run()
