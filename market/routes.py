from market import app
from flask import render_template
from market.models import Item


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


# @app.route('/about')
# def about():
#     return f'<h1>test</h1>'

# @app.route('/about/<username>')
# def custAbout(username):
#     return f'<h1>Hello {username}</h1>'