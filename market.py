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
