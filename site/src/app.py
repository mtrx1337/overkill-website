from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('index.html')
    return 'hello world'

@app.route('/cv')
def cv():
    return render_template('cv.html')
