from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    
    names       = StringField('Nombres', validators=[DataRequired()])
    lastnames   = StringField('Apellidos', validators=[DataRequired()])
    #type       = SelectField('Tipo', validators=[DataRequired()],choices=[('DNI', 'Cedula'), ('PSPT', 'Pasaporte')])
    dni         = StringField('Identificación', validators=[DataRequired()])
    #gender      = SelectField('Género', validators=[DataRequired()],choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    #status      = SelectField('Estadi', validators=[DataRequired()],choices=[('A', 'Activo'), ('I', 'Inactivo')])
    #url_picture = StringField('URL de Sistema', validators=[DataRequired()])
    submit      = SubmitField('Guardar')

