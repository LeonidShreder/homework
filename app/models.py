from sqlalchemy import orm
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy, sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import sqlamp

Base = Declarative_base()

class Categories(Base):
    __tablename__ = 'categories'
    name = db.Column(db.String(), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.String(), unique=True)
    parent_id = db.Column(Integer, ForeignKey('Categories.id'))



