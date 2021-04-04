from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# the app is this file
app = Flask(__name__)

# if an external library needs additional info from us then we pass it here
# this is the config for the sqlite3 db I created
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '80d8f791fa2ce3b7f4dc347f'
# thid line links the db to this file
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from market import routes