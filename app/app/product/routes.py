import os
from flask import render_template, current_app as app, request, session, redirect, url_for, jsonify
from . import product


@app.route('/product')
def product():
    return render_template('index.html')


@app.route('/product/register/<product>')
def product_register(product=None):
    return render_template('index.html', product=product)
