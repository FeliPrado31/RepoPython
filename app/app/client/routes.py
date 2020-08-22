import os
from flask import flash, json, make_response, render_template, current_app as app, request, session, redirect, url_for, jsonify
from . import client
from .models import Client, ClientSchema
from .form import ClientUpload
# import uploads for pothos
from flask_uploads import configure_uploads, IMAGES, UploadSet
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/client', methods=['GET', 'POST'])
def client_home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('client/index.html')
    # try:
    #     form = ClientUpload()

    #     if form.validate_on_submit():
    #         print(form)
    #         # client = Client(request.form.get('name'), request.form.get(
    #         #     'cc'), request.form.get('tel'), form.image.data, request.form.get('address'))
    #         # client.save()
    #         return 'Work', 201
    #     return 'Error', 404
    # except Exception as e:
    #     return jsonify({"error": e})


@app.route('/client/edit/<int:id>', methods=['PUT'])
def client_edit(id=None):
    if request.method == 'PUT':
        try:
            data = client.get_by_id(id)
            if data != None:
                data.name = request.json['name']
                data.category = request.json['category']
                data.price = request.json['price']
                data.count = request.json['count']
                data.state = request.json['state']
                client.update()
                client_schema = ClientSchema()
                return client_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})


@app.route('/client/<int:id>', methods=['GET'])
def client_get(id=None):
    if request.method == 'GET':
        try:
            data = client.get_by_id(id)
            if data != None:
                client_schema = ClientSchema()
                return client_schema.jsonify(data)
            else:
                return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return jsonify({"error": e})
