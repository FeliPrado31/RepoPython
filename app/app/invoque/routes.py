import datetime
import os
import collections
import requests
from flask import json, flash, make_response, render_template, current_app as app, request, session, redirect, url_for, jsonify
from . import invoque
from .models import Invoque, InvoqueSchema


@app.route('/invoque')
def get_invoque():
    r = requests.get('http://localhost:8080/invoque/all')
    return render_template('/invoque/index.html', invoque=r.json())


@app.route('/invoque/new')
def invoque_new():
    return render_template('/invoque/new.html')


@app.route('/invoque/all', methods=['GET'])
def invoque_all():
    invoque = Invoque.query.all()
    invoque_schema = InvoqueSchema(many=True)
    return invoque_schema.jsonify(invoque)


@app.route('/invoque/create', methods=['POST'])
def invoque_register():
    if request.method == 'POST':
        try:
            products = request.form['products']
            total = request.form['price']
            billing_method = request.form['billing_method']
            client_id = request.form['client_id']

            r = requests.get(f'http://localhost:8080/product/{products}')
            if r.status_code == 404:
                flash("Sorry. This Product don't exist.")
                return redirect(url_for('invoque_new'))

            c = requests.get(f'http://localhost:8080/client/{client_id}')
            if r.status_code == 404:
                flash("Sorry. This client don't exist.")
                return redirect(url_for('invoque_new'))


            buy = requests.get(f'http://localhost:8080/client/buy/{client_id}')
            # this part is only with the system of multiple buys
            
            # findInvoque = Invoque.query.filter_by(client_id=client_id).first()

            # if findInvoque != None:
            #     findInvoque.total = int(findInvoque.total) + int(total)
            #     findInvoque.products = findInvoque.products + ', ' + products
            #     findInvoque.billing_method = billing_method
            #     findInvoque.num_products = findInvoque.num_products + 1
            #     findInvoque.save()
            #     invoque_schema = InvoqueSchema()
            #     return redirect(url_for('invoque_new'))
            invoque = Invoque(products, total, billing_method,
                              client_id, 1, datetime.datetime.utcnow())
            invoque.save()
            invoque_schema = InvoqueSchema()
            return redirect(url_for('invoque_new'))

        except Exception as e:
            return jsonify({"error": e})



@app.route('/invoque/<int:id>', methods=['GET'])
def invoque_by_id(id=None):
    if request.method == 'GET':
        try:
            data = Invoque.get_by_id(id)
            if data != None:
                invoque_schema = InvoqueSchema()
                return invoque_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return redirect(url_for('get_invoque'))


@app.route('/invoque/edit/<int:id>', methods=['GET'])
def invoque_edit_view(id=None):
    r = requests.get(f'http://localhost:8080/invoque/{id}')
    return render_template('invoque/edit.html', invoque=r.json())


@app.route('/invoque/update', methods=['POST'])
def invoque_update():
    if request.method == 'POST':
        try:
            data = Invoque.get_by_id(request.form['id'])
            if data != None:
                data.billing_method = request.form['billing_method']
                Invoque.update()
                return redirect(url_for('get_invoque'))
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})
