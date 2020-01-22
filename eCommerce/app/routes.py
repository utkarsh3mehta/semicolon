from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.models import Category, Product
@app.route('/')
def index():
    return "This is Semicolon eCommerce API"

@app.route('/product/', methods=['GET','POST'])
@app.route('/product/<int:productid>', methods=['GET','POST'])

@app.route('/category/', methods=['GET','POST'])
@app.route('/category/<int:categoryid>', methods=['GET','POST'])
