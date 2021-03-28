from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# the app is this file
app = Flask(__name__)

# if an external library needs additional info from us then we pass it here
# this is the config for the sqlite3 db I created
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# thid line links the db to this file
db = SQLAlchemy(app)

from market import routes