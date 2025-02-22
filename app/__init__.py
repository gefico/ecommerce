from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
app.secret_key = 'some_secret'
db = SQLAlchemy(app)

from app import  models, routes