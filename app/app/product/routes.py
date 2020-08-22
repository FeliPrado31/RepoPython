import os
import requests
from flask import json, make_response, render_template, current_app as app, request, session, redirect, url_for, jsonify
from . import product
from .models import Product, ProductSchema


@app.route('/product')
def getView(product=None):
    r = requests.get('http://localhost:8080/product/all')
    return render_template('/product/index.html', products=r.json())


@app.route('/product/all', methods=['GET'])
def product():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return product_schema.jsonify(products)


@app.route('/product/create', methods=['POST'])
def product_register():
    if request.method == 'POST':
        try:
            name = request.json['name']
            category = request.json['category']
            price = request.json['price']
            count = request.json['count']
            state = request.json['state']
            product = Product(name, category, price, count, state)
            product.save()

            product_schema = ProductSchema()
            return product_schema.jsonify(product)
        except Exception as e:
            return jsonify({"error": e})


@app.route('/product/edit/', methods=['PUT'])
def product_change_state():
    if request.method == 'PUT':
        try:
            print(request.form['delete'])
            # data = Product.get_by_id(id)
            # if data != None:
            #     data.state = False
            #     Product.update()
            #     product_schema = ProductSchema()
            #     return product_schema.jsonify(data)
            # else:
            #     return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
           return jsonify({"error": e})

@app.route('/product/edit/<int:id>', methods=['PUT'])
def product_edit(id=None):
    if request.method == 'PUT':
        try:
            data = Product.get_by_id(id)
            if data != None:
                data.name = request.json['name']
                data.category = request.json['category']
                data.price = request.json['price']
                data.count = request.json['count']
                data.state = request.json['state']
                Product.update()
                product_schema = ProductSchema()
                return product_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})


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
