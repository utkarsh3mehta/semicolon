from flask import jsonify, request, url_for

from app import db
from app.api import bp
from app.api.errors import bad_request
from app.models import Category, Product


@bp.route('/category/', methods=['GET','POST'])
@bp.route('/category/<int:categoryid>', methods=['GET','PUT'])
def category(categoryid=None):
    if request.method == 'GET':
        if categoryid is not None:
            return jsonify(Category.query.get_or_404(categoryid).serialize())
        else:
            return jsonify(Category.serialize_list(Category.query.all()))
    else:
        if categoryid is not None:
            c = Category.query.get_or_404(categoryid)
            data = request.get_json() or {}
            if 'category_name' in data and data['category_name'] != c.category_name and Category.query.filter_by(category_name=data['category_name']).first():
                return bad_request('ID and name do not match. You are trying to edit another category\'s details.' )
            c.from_dict(data)
            db.session.commit()
            response = jsonify(c.serialize())
            response.statuscode = 201
            response.headers['Location'] = url_for('api.category', categoryid=c.id)
            return response
        else:
            data = request.get_json() or {}
            if 'category_name' not in data or 'category_image' not in data:
                return bad_request('Must include name, image fields')
            if Category.query.filter_by(category_name=data['category_name']).first():
                return bad_request('A category with the same name already exists')
            c = Category()
            c.from_dict(data)
            db.session.add(c)
            db.session.commit()
            response = jsonify(c.serialize())
            response.statuscode = 201
            response.headers['Location'] = url_for('api.category', categoryid=c.id)
            return response

@bp.route('/category/<int:categoryid>/product/', methods=['GET'])
def category_product(categoryid):
    c = Category.query.get(categoryid)
    return jsonify(Product.serialize_list(Product.query.filter_by(category=c)))

@bp.route('/category/<int:categoryid>', methods=['DELETE'])
def del_category(categoryid):
    c = Category.query.get_or_404(categoryid)
    db.session.delete(c)
    db.session.commit()
    response = jsonify(f'Category with name: {c.category_name} and id: {c.id} deleted')
    response.statuscode = 201
    return response