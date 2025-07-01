
from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional,Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SelectField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

class ContactForm(FlaskForm):
    name = StringField('Nombre completo', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    phone = StringField('Teléfono', validators=[Optional()])
    company = StringField('Empresa', validators=[Optional()])
    event_type = SelectField('Tipo de evento', choices=[
        ('', 'Seleccione'),
        ('corporativo', 'Corporativo'),
        ('social', 'Social'),
        ('feria', 'Feria'),
        ('otro', 'Otro')
    ], validators=[Optional()])
    event_date = DateField('Fecha tentativa', format='%Y-%m-%d', validators=[Optional()])
    attendees = IntegerField('Número de asistentes', validators=[Optional()])
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

class ServiceForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    icon = StringField('Clase de ícono Bootstrap', validators=[DataRequired()])
    submit = SubmitField('Guardar')


class AboutForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    paragraph1 = TextAreaField('Párrafo Principal', validators=[DataRequired()])
    paragraph2 = TextAreaField('Párrafo Secundario', validators=[DataRequired()])
    image = FileField('Imagen', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Sólo imágenes.')
    ])
    submit = SubmitField('Guardar')

class AboutFeatureForm(FlaskForm):
    
    icon = StringField('Ícono (clase Bootstrap)', validators=[DataRequired()])
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Guardar')


class TeamMemberForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    role = StringField('Cargo', validators=[DataRequired()])
    description = TextAreaField('Descripción (opcional)')
    photo = FileField('Foto', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Sólo imágenes.')
    ])
    submit = SubmitField('Guardar')

class AdvantageForm(FlaskForm):
    icon = StringField('Ícono (Bootstrap)', validators=[DataRequired()])
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class ProjectForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    image = FileField('Imagen Principal', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Sólo imágenes.')
    ])
    submit = SubmitField('Guardar')

class HomeSlideForm(FlaskForm):
    image = FileField('Imagen', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Solo imágenes')
    ])
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    submit = SubmitField('Guardar')

class HomeWelcomeForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    paragraph = TextAreaField('Párrafo', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class HomeFeatureForm(FlaskForm):
    icon = StringField('Ícono (Emoji o clase Bootstrap)')
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    submit = SubmitField('Guardar')

