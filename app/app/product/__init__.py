from flask import Blueprint
product = Blueprint('product', __name__,
                   template_folder='templates', static_folder='static')

from . import routes, models
