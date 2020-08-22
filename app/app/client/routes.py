import os
import requests
from flask import json, make_response, render_template, current_app as app, request, session, redirect, url_for, jsonify
from . import client
from .models import Client, ClientSchema


@app.route('/client')
def client():
    r = requests.get('http://localhost:8080/client/all')
    return render_template('client/index.html', clients=r.json())

@app.route('/client/top')
def client_most():
    r = requests.get('http://localhost:8080/client/most')
    return render_template('client/mostClient.html', clients=r.json())


@app.route('/client/new')
def client_new():
    return render_template('client/new.html')


@app.route('/client/create', methods=['POST'])
def client_register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            cc = request.form['cc']
            telephone = request.form['tel']
            photo = request.form['link']
            addres = request.form['address']
            client = Client(name, cc, telephone, photo, addres, 1)
            client.save()

            client_schema = ClientSchema()
            return redirect(url_for('client'))
        except Exception as e:
            return redirect(url_for('client_register'))


@app.route('/client/edit', methods=['GET'])
def client_edit_view():
    return render_template('client/edit.html')


@app.route('/client/delete/<int:id>', methods=['DELETE'])
def client_delete_by_id(id=None):
    if request.method == 'DELETE':
        try:
            Client.query.filter(Client.id == id).delete()
            Client.update()
            return redirect(url_for('client'))
        except Exception as e:
            return jsonify({"error": e})


@app.route('/client/update', methods=['POST'])
def client_edit():
    if request.method == 'POST':
        try:
            data = Client.get_by_id(request.form['id'])
            if data != None:
                data.name = request.form['name']
                data.cc = request.form['cc']
                data.photo = request.form['link']
                data.telephone = request.form['tel']
                data.address = request.form['address']
                Client.update()
                client_schema = ClientSchema()
                return redirect(url_for('client'))
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})


@ app.route('/client/buy/<int:id>', methods=['GET'])
def client_new_buy(id=None):
    if request.method == 'GET':
        try:
            data = Client.get_by_id(id)
            if data != None:
                data.count = data.count + 1
                data.save()
                client_schema = ClientSchema()
                return client_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})


@ app.route('/client/<int:id>', methods=['GET'])
def client_get(id=None):
    if request.method == 'GET':
        try:
            data = Client.get_by_id(id)
            if data != None:
                client_schema = ClientSchema()
                return client_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})



@app.route('/client/most', methods=['GET'])
def invoque_by_most():
    data = Client.get_most_buyer()
    invoque_schema = ClientSchema(many=True)
    return invoque_schema.jsonify(data)

@ app.route('/client/all', methods=['GET'])
def client_all():
    client = Client.query.all()
    client_schema = ClientSchema(many=True)
    return client_schema.jsonify(client)
