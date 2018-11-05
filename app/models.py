from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class phones(db.Model):
    __tablename__ = 'phones'

    name = db.Column(db.String(), index=True, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    db.phones.insert( {_name:'Phones', path: null})
    db.phones.insert( {_name:'Iphone', path: 'phones'})
    db.phones.insert( {_name:'Color', path: 'phones, Iphone'})
    db.phones.insert({_name: 'Gold', path: 'phones, Iphone, Color'})
    db.phones.insert({_name: 'Black', path: 'phones, Iphone, Color'})
    db.phones.insert({_name: 'Pink', path: 'phones, Iphone, Color'})
    db.phones.insert({_name: 'Memory', path: 'phones, Iphone'})
    db.phones.insert({_name: '64', path: 'phones, Iphone, Memory'})
    db.phones.insert({_name: '128', path: 'phones, Iphone, Memory'})
    db.phones.insert({_name: '256', path: 'phones, Iphone, Memory'})
    db.phones.insert({_name: 'Xiaomi', path: 'phones'})
    db.phones.insert({_name: 'MI8', path: 'phones, Xiaomi'})
    db.phones.insert({_name: 'MI_MIX3', path: 'phones, Xiaomi'})
    db.phones.insert({_name: 'Color', path: 'phones, Xiaomi, MI_MIX3'})
    db.phones.insert({_name: 'Memory', path: 'phones, Xiaomi, MI_MIX3'})


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>' .format(self.id)
