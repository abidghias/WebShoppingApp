from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import logging

#enabling logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)
logging.warning('This will get logged to a file')

#initializing the flask app with credentials
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WebAppDatabase.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

#initializing a database 
db = SQLAlchemy(app)

#used for password hashing
bcrypt = Bcrypt(app)

#inbuilt logging implementation
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes