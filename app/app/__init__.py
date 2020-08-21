# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__, static_url_path='/static')

# Configurations
app.config.from_object('config')

app.app_context().push()

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
db.create_all()
# Sample HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from .product import product
app.register_blueprint(product)