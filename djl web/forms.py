from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SelectField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class ImageUploadForm(FlaskForm):
    album = SelectField('Álbum', coerce=int, validators=[DataRequired()])
    images = FileField(
        'Imágenes',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Solo imágenes')
        ],
        render_kw={"multiple": True}
    )
    submit = SubmitField('Subir Imágenes')

ICON_CHOICES = [
    ('bi-briefcase', 'Briefcase'),
    ('bi-gear', 'Gear'),
    ('bi-lightbulb', 'Lightbulb'),
    ('bi-bar-chart', 'Bar Chart'),
    ('bi-people', 'People'),
    ('bi-megaphone', 'Megaphone'),
    ('bi-palette', 'Palette'),
    ('bi-globe', 'Globe'),
    ('bi-calendar-event', 'Calendar Event'),
    ('bi-award', 'Award'),
    ('bi-camera', 'Camera'),
    ('bi-music-note', 'Music Note'),
    ('bi-shop', 'Shop'),
    ('bi-laptop', 'Laptop'),
    ('bi-badge-ad', 'Ad Badge')

]

class ServiceForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    icon = SelectField('Ícono', choices=ICON_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Guardar')



