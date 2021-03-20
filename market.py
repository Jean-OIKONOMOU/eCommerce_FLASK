from flask import Flask
from flask import render_template
app = Flask(__name__)

# export FLASK_APP=market.py
# export FLASK_DEBUG=1
# flask run

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# @app.route('/about')
# def about():
#     return f'<h1>test</h1>'

# @app.route('/about/<username>')
# def custAbout(username):
#     return f'<h1>Hello {username}</h1>'
