from apps.faceapi import blueprint
from flask import current_app, render_template, request, redirect, url_for, jsonify, flash
from werkzeug.utils import secure_filename
from .services import *
from .forms import * 
import face_recognition
import os

@blueprint.route('/')
def index():
    return "Hello world"

@blueprint.route('/users', methods=['GET','POST'])
def users():
    user_form = UserForm(request.form)  
    if request.method == 'POST':
        f = request.files['logo']
        if f:
            _, file_extension = os.path.splitext(f.filename)
            filename = secure_filename(user_form.dni.data+file_extension)
            directorie = os.path.join(current_app.config['DIRBASE'],'static','assets','uploads', filename)
            f.save(directorie)
            image = face_recognition.load_image_file(directorie)
            encoding = face_recognition.face_encodings(image)
            if len(encoding) == 1:
                encoding = encoding[0]
                process =True
            else:
                process =False
                flash('Debe estar el rostro del usuario en la imagen')
        else:
            process =False
            flash('Foto del usuario es requerido','error')
            pass
        if process:
            result = setUser(encoding, filename, request.form)
            msn = "Usuario agregado exitoamente!" if result else "Problemas con el registro del usuario"
            flash(msn, 'success' if result else 'error')
    items = getUsers()
    
    return render_template('index.html', form=user_form, users=items)

@blueprint.route('/user/<int:user_id>', methods=['GET','PUT','DELETE'])
def user(user_id):
    users = getUsers()
        
    known_faces = [item.encoding  for item in users]
    
    directorie = os.path.join(current_app.config['DIRBASE'],'static','assets','uploads', 'obama2.jpg')
    unknown_image = face_recognition.load_image_file(directorie)
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    print(results)

    return jsonify({"results":str(results)})