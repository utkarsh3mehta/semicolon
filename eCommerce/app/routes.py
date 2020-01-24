from app import app
from flask import jsonify

@app.route('/')
def index():
    api = {
        "#WELCOME MESSAGE": "This is semicolon eCommerce API.",
        "GET all products": "/api/v1/product/",
        "GET one product": "/api/v1/product/<int:productid>",
        "ADD product": {
            "#uri": "/api/v1/product/",
            "details needed": {
                "product_name": "string !important",
                "product_description": "string",
                "product_price": "integer/string !important",
                "product_image": "string/path"
            }
        },
        "UPDATE product": "/api/v1/product/<int:productid>",
        "DELETE product": "/api/v1/product/<int:productid>",
        "GET all categories": "/api/v1/category/",
        "GET one category": "/api/v1/category/<int:categoryid>",
        "ADD category": {
            "#uri": "/api/v1/category/",
            "details needed": {
                "category_name": "string !important",
                "category_description": "string",
                "category_image": "string/path !important"
            }
        },
        "UPDATE category": "/api/v1/category/<int:categoryid>",
        "DELETE category": "/api/v1/category/<int:categoryid>"
    }
    return jsonify(api)