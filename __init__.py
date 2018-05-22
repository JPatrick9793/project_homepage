#! --shebang

from flask import Flask 
from flask import url_for
from flask import render_template

app = Flask(__name__) 

@app.route('/') 
def hello_world():
    return render_template('index.html')

@app.route('/Resume')
def getResumePage():
    #return render_template('resume.html')
    return ("This will be my resume page")

@app.route('/Projects')
def getProjectsPage():
    #return render_template('resume.html')
    return ("This will be my projects page")

@app.route('/Skills')
def getSkillsPage():
    #return render_template('resume.html')
    return ("This will be my skills page")

@app.route('/About_me')
def getAboutMePage():
    #return render_template('resume.html')
    return ('This will be my "About me" page')

@app.route('/Contact_me')
def getContactMePage():
    #return render_template('resume.html')
    return ('This will be my "Contact Me" page')

if __name__ == '__main__':
    app.run()
