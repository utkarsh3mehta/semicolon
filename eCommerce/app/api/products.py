from flask import jsonify, request, url_for

from app import db
from app.api import bp
from app.models import Product
from app.api.errors import bad_request


@bp.route('/product/', methods=['GET','POST'])
@bp.route('/product/<int:productid>', methods=['GET','POST'])
def product(productid=None):
    if request.method == 'GET':
        if productid is not None:
            return jsonify(Product.query.get_or_404(productid).serialize())
        else:
            return jsonify(Product.serialize_list(Product.query.all()))
    elif request.method == 'POST':
        if productid is not None:
            return 'this is put'
        else:
            data = request.get_json() or {}
            if 'product_name' not in data or 'product_price' not in data or 'category_id' not in data:
                return bad_request('Must include name, price and category fields')
            if Product.query.filter_by(product_name=data['product_name']).first():
                return bad_request('A product with the same name already exists')
            p = Product()
            p.from_dict(data)
            db.session.add(p)
            db.session.commit()
            response = jsonify(p.serialize())
            response.statuscode = 201
            response.headers['Location'] = url_for('api.product', productid=p.id)
            return response