from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# the app is this file
app = Flask(__name__)
# if an external library needs additional info from us then we pass it here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# the db is linked to this file
db = SQLAlchemy(app)

# export FLASK_APP=market.py
# export FLASK_DEBUG=1
# flask run
