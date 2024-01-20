from apps.faceapi import blueprint
from apps import db
from flask import current_app, render_template, request, redirect, url_for, jsonify, flash, send_from_directory
from werkzeug.utils import secure_filename
from .services import *
from .forms import * 
import os

@blueprint.route('/')
def index():
    debug = current_app.config.get('DEBUG')
    print('DEBUG --> '.format(debug))
    return "Hello world"

@blueprint.route('/users', methods=['GET','POST'])
def users():
    user_form = UserForm(request.form)  
    items = []
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join('upload', filename))
        return send_from_directory('upload', filename)

        # create a new Contact object
        new_contact = User(**request.form)
        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Usuario agregado exitosamente!')

        return redirect(url_for('contacts.index'))
    else:
        items = getUsers()
    
    return jsonify({"items":items})

@blueprint.route('/user/<int:user_id>', methods=['GET','PUT','DELETE'])
def user(user_id):
    item = getUser(user_id)
    return jsonify({"item":item if item else {}})