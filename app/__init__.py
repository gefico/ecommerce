from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
app.secret_key = 'e5af987a9e549494c0c9959a893f4a9f'  # Defina uma chave secreta
db = SQLAlchemy(app)

from app import  models, routes