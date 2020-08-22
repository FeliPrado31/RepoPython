from flask import Blueprint
invoque = Blueprint('invoque', __name__,
                   template_folder='../templates', static_folder='static')


from . import routes, models
