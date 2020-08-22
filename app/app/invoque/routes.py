import os
import requests
from flask import json, make_response, render_template, current_app as app, request, session, redirect, url_for, jsonify
from . import product
from .models import Product, ProductSchema


@app.route('/product')
def getView(product=None):
    r = requests.get('http://localhost:8080/product/all')
    return render_template('/product/index.html', products=r.json())

@app.route('/product/new')
def product_new():
    return render_template('product/new.html')


@app.route('/product/all', methods=['GET'])
def product():
    products = Product.query.filter(Product.state == True)
    product_schema = ProductSchema(many=True)
    return product_schema.jsonify(products)


@app.route('/product/create', methods=['POST'])
def product_register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            category = request.form['category']
            price = request.form['price']
            count = request.form['count']
            product = Product(name, category, price, count)
            product.save()

            return redirect(url_for('getView'))
        except Exception as e:
            return jsonify({"error": e})


@app.route('/product/state/<int:id>', methods=['PUT'])
def product_change_state(id=None):
    if request.method == 'PUT':
        try:
            data = Product.get_by_id(id)
            if data != None:
                data.state = False
                Product.update()
                product_schema = ProductSchema()
                return product_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
           return jsonify({"error": e})

@app.route('/product/delete/<int:id>', methods=['DELETE'])
def product_delete_by_id(id=None):
    if request.method == 'DELETE':
        try:
            Product.query.filter(Product.id == id).delete()
            Product.update()
            return redirect(url_for('getView'))
        except Exception as e:
            return jsonify({"error": e})

@app.route('/product/update', methods=['POST'])
def product_update():
    if request.method == 'POST':
        try:
            data = Product.get_by_id(request.form['id'])
            if data != None:
                data.name = request.form['name']
                data.category = request.form['category']
                data.price = request.form['price']
                data.count = request.form['count']
                Product.update()
                product_schema = ProductSchema()
                return redirect(url_for('getView'))
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})


@app.route('/product/edit', methods=['GET'])
def product_edit_view():
    return render_template('product/edit.html')

@app.route('/product/<int:id>', methods=['GET'])
def product_get(id=None):
    if request.method == 'GET':
        try:
            data = Product.get_by_id(id)
            if data != None:
                product_schema = ProductSchema()
                return product_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})
