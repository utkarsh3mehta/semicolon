from flask import jsonify, request, url_for

from app import db
from app.api import bp
from app.models import Product
from app.api.errors import bad_request


@bp.route('/v1/product/', methods=['GET','POST'])
@bp.route('/v1/product/<int:productid>', methods=['GET','PUT'])
def product(productid=None):
    if request.method == 'GET':
        if productid is not None:
            return jsonify(Product.query.get_or_404(productid).serialize())
        else:
            return jsonify(Product.serialize_list(Product.query.all()))
    else:
        if productid is not None:
            p = Product.query.get_or_404(productid)
            data = request.get_json()
            if 'product_name' in data and data['product_name'] != p.product_name and Product.query.filter_by(product_name=data['product_name']).first():
                return bad_request('ID and Name do not match. You are trying to edit another product\'s details')
            p.from_dict(data)
            db.session.commit()
            response = jsonify(p.serialize())
            response.statuscode = 201
            response.headers['Location'] = url_for('api.product', productid=p.id)
            return response
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

@bp.route('/v1/product/<int:productid>', methods=['DELETE'])
def del_product(productid):
    p = Product.query.get_or_404(productid)
    db.session.delete(p)
    db.session.commit()
    response = jsonify(f'Product with name: {p.product_name} and id: {p.id} deleted')
    response.statuscode = 201
    return response