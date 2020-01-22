from app import db
from datetime import datetime
class Category(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(128), index=True, unique=True)
    category_description = db.Column(db.String(500))
    category_image = db.Column(db.String(200), nullable=False)
    category_addedOn = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    products = db.relationship('Product', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category: {}>'.format(self.category_name)
