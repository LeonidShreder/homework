from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.config.from_object(Config)
app.config.from_pygile('config.py')

db = SQLAlchemy(app)
