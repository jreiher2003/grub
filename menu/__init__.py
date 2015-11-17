from flask import Flask 
from sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////menu.db'
db = SQLAlchemy(app)
app.debug = True

from menu import views