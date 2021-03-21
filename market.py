from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# the app is this file
app = Flask(__name__)
# if an external library needs additional info from us then we pass it here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# the db is linked to this file
db = SQLAlchemy(app)


# WARNING : after creating your model you should go in a Python shell and type 'from market import db' then 'db.create_all()'. Market being the value of __name__. This creates an SQL db.
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False,
                            unique=True)


# export FLASK_APP=market.py
# export FLASK_DEBUG=1
# flask run


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [{
        'id': 1,
        'name': 'Phone',
        'barcode': '893212299897',
        'price': 500
    }, {
        'id': 2,
        'name': 'Laptop',
        'barcode': '123985473165',
        'price': 900
    }, {
        'id': 3,
        'name': 'Keyboard',
        'barcode': '231985128446',
        'price': 150
    }]
    return render_template('market.html', items=items)


# @app.route('/about')
# def about():
#     return f'<h1>test</h1>'

# @app.route('/about/<username>')
# def custAbout(username):
#     return f'<h1>Hello {username}</h1>'
