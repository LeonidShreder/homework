from sqlalchemy import orm
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy, sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import sqlamp

Base = declarative_base()
"""in this db i have 3 columns name id and categories_path"""
class categories(Base):
    __tablename__ = 'categories'
    name = db.Column(db.String(), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    categories_path = db.Column(Integer, ForeignKey('categories.id'))

    def __init__(self, name, id, categories_path):
        self.name = name
        self.id = id
        self.categories_path = categories_path


