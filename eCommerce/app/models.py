from app import db
from datetime import datetime
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class Category(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(128), index=True, unique=True)
    category_description = db.Column(db.String(500))
    category_image = db.Column(db.String(200), nullable=False)
    category_addedOn = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    products = db.relationship('Product', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category: {}>'.format(self.category_name)

class Product(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(128), index=True, unique=True)
    product_description = db.Column(db.String(500))
    product_price = db.Column(db.Integer, nullable=False)
    product_image = db.Column(db.String(200))
    product_addedOn = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Product: {}>'.format(self.product_name)

    def serialize(self):
        p = Serializer.serialize(self)
        p['category'] = Category.query.get(self.category_id).category_name
        return p
