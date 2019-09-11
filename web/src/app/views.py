from flask import Flask, render_template
from app import app
import sys

@app.route('/')
def index():
    #return render_template('index.html')
    return 'hello world'

@app.route('/cv')
def cv():
    return render_template('cv.html')
