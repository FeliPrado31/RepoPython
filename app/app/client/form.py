from flask_wtf import FlaskForm
from wtforms import FileField

class ClientUpload(FlaskForm):
    image = FileField('image')

