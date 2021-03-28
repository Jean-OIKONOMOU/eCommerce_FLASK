from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# the app is this file
app = Flask(__name__)

# if an external library needs additional info from us then we pass it here
# this is the config for the sqlite3 db I created
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# the db is linked to this file
db = SQLAlchemy(app)

# here are the routes of the web page
from market import routes

# export FLASK_APP=market.py
# export FLASK_DEBUG=1
# flask run
