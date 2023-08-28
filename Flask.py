from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Ajith</h1> <p>I completed mine Under Graduation in the stream of Computer Application<br>at Achariya Arts and Science College (which is affiliated with Pondicherry University)<br>in the Academic year of 2017 - 2020.</p>'

@app.route('/about')
def about():
    return '<h3> Learning Flask </h3>'

@app.route('/contact')
def content():
    return '<h3> CONTACT : Learning Flask </h3>'

@app.route('/users/<name>')
def users(name):
    return '<h3>Welcome {}</h3>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
