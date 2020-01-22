from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField, SubmitField
from wtforms.validators import Required, DataRequired, ValidationError #, FileRequired
from app.models import Product, Category

categories = Category.query.all()
something = []
for cat in categories:
    something.append((cat.id, cat.category_name))

class AddProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_description = StringField('Product Description')
    product_price = StringField('Product Price', validators=[DataRequired()])
    product_image = FileField('Product Image')
    category = SelectField('Category', choices=something, coerce=int, validators=[Required()])
    submit = SubmitField('Add New Product')

    def validate_product_name(self, product_name):
        prod = Product.query.filter_by(product_name=product_name.data).first()
        if prod is not None:
            raise ValidationError('A product with the same name already exists')

class AddCategoryForm(FlaskForm):
    category_name = StringField('Category Name', validators=[DataRequired()])
    category_description = StringField('Category Description')
    category_image = FileField('Category Image', validators=[Required()])
    submit = SubmitField('Add New Category')

    def validate_category_name(self, category_name):
        cat = Category.query.filter_by(category_name=category_name.data).first()
        if cat is not None:
            raise ValidationError('A category with the same name already exists')