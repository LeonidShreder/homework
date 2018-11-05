from app import db

class categories(db.Model):

    __tablename__ = 'categories'

    name_of_category = db.Column(db.String(64), index=True, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    1.2 = db.relationship('mobilephone', backref='type_of_category')
    1.3 = db.relationship('laptop', backref='type_of_category')
    1.4 = db.relationship('headphones', primary_key=True)



    def __repr__(self):
        return '<categories {}>' .format(self.name_of_category, self.Global_id, self.id)
