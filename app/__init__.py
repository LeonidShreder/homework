from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import app.views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()