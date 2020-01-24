from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.models import Category, Product

@app.route('/')
def index():
    return "This is Semicolon eCommerce API"

@app.route('/product/', methods=['GET','POST'])
@app.route('/product/<int:productid>', methods=['GET','POST'])
def product(productid=None):
    if request.method == 'GET':
        if productid is not None:
            return jsonify(Product.query.get_or_404(productid).serialize())
        else:
            return jsonify(Product.serialize_list(Product.query.all()))
    elif request.method == 'POST':
        if productid is not None:
            return 'This is put'
        else:
            # product_name = request.form['product_name']
            # product_description = request.form['product_description']
            # product_price = request.form['product_price']
            # product_image = request.form['product_image']
            # category = request.form['category']
            data = request.get_json() or {}
            if 'product_name' not in data:
                raise ValueError('Product name is a required field')
            if 'product_price' not in data:
                raise ValueError('Product price is a required field')
            if 'category' not in data:
                raise ValueError('Product category is a required field')
            p = Product()
            p.from_dict(data)
            db.session.add(p)
            db.session.commit()
            return 'Product added'

@app.route('/category/', methods=['GET','POST'])
@app.route('/category/<int:categoryid>', methods=['GET','POST'])
def category(categoryid=None):
    form = AddCategoryForm()
    if form.validate_on_submit():
        c = Category(category_name=form.category_name.data, category_description=form.category_description.data,category_image=form.category_image.data)
        db.session.add(c)
        db.session.commit()
        flash('New category added')
        return redirect(url_for('category'))
    return render_template('add_category.html',form=form)