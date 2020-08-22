from flask import Blueprint
client = Blueprint('client', __name__,
                   static_folder='static',template_folder='templates')


from . import routes, models
