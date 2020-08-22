# Import flask and template operators
from flask import Flask, render_template

#Import CORS
from flask_cors import CORS


# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#Import Marshmallow
from flask_marshmallow import Marshmallow




# Define the WSGI application object
app = Flask(__name__, static_url_path='/static')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configurations
app.config.from_object('config')

app.app_context().push()

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

db.create_all()
db.session.commit()

#configure images

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from .product import product
app.register_blueprint(product)

from .client import client
app.register_blueprint(client)