from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from config import Config
from models import About, AboutFeature, Advantage, Album, Project, Service, TeamMember, db, User, GalleryImage, ContactMessage
from forms import AboutFeatureForm, AboutForm, AdvantageForm, ImageUploadForm, LoginForm, ContactForm, ProjectForm, ServiceForm, TeamMemberForm
import os
import uuid 


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'
mail = Mail(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def about():
    about = About.query.first()
    features = AboutFeature.query.all()
    team = TeamMember.query.all()
    return render_template('about.html', about=about, features=features, team=team)

@app.route('/servicios')
def services():
    services = Service.query.all()
    advantages = Advantage.query.all()    
    projects = Project.query.all()
    print(projects)
    return render_template('services.html', services=services, advantages=advantages, projects=projects)

@app.route('/galeria')
def galeria():
    albums = Album.query.all()
    return render_template('galeria.html', albums=albums)

# Listar proyectos
@app.route('/admin/projects')
@login_required
def admin_projects():
    projects = Project.query.all()
    return render_template('admin_projects.html', projects=projects)

# Añadir proyecto
@app.route('/admin/projects/add', methods=['GET', 'POST'])
@login_required
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        filename = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(app.static_folder, 'images/proyects', filename))

        project = Project(
            title=form.title.data,
            description=form.description.data,
            image_filename=filename
        )
        db.session.add(project)
        db.session.commit()
        flash('Proyecto añadido.', 'success')
        return redirect(url_for('admin_projects'))
    return render_template('admin_project_form.html', form=form)

# Editar proyecto
@app.route('/admin/projects/edit/<int:project_id>', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        if form.image.data:
            if project.image_filename:
                old_path = os.path.join(app.static_folder, 'images/proyects', project.image_filename)
                if os.path.exists(old_path):
                    os.remove(old_path)
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(app.static_folder, 'images/proyects', filename))
            project.image_filename = filename
        project.title = form.title.data
        project.description = form.description.data
        db.session.commit()
        flash('Proyecto actualizado.', 'success')
        return redirect(url_for('admin_projects'))
    return render_template('admin_project_form.html', form=form, project=project)

# Eliminar proyecto
@app.route('/admin/projects/delete/<int:project_id>', methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.image_filename:
        path = os.path.join(app.static_folder, 'images/proyects', project.image_filename)
        if os.path.exists(path):
            os.remove(path)
    db.session.delete(project)
    db.session.commit()
    flash('Proyecto eliminado.', 'success')
    return redirect(url_for('admin_projects'))


# Listar ventajas
@app.route('/admin/advantages')
@login_required
def admin_advantages():
    advantages = Advantage.query.all()
    return render_template('admin_advantages.html', advantages=advantages)

# Añadir ventaja
@app.route('/admin/advantages/add', methods=['GET', 'POST'])
@login_required
def add_advantage():
    form = AdvantageForm()
    if form.validate_on_submit():
        advantage = Advantage(
            icon=form.icon.data,
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(advantage)
        db.session.commit()
        flash('Ventaja añadida.', 'success')
        return redirect(url_for('admin_advantages'))
    return render_template('admin_advantage_form.html', form=form)

# Editar ventaja
@app.route('/admin/advantages/edit/<int:advantage_id>', methods=['GET', 'POST'])
@login_required
def edit_advantage(advantage_id):
    advantage = Advantage.query.get_or_404(advantage_id)
    form = AdvantageForm(obj=advantage)
    if form.validate_on_submit():
        advantage.icon = form.icon.data
        advantage.title = form.title.data
        advantage.description = form.description.data
        db.session.commit()
        flash('Ventaja actualizada.', 'success')
        return redirect(url_for('admin_advantages'))
    return render_template('admin_advantage_form.html', form=form, advantage=advantage)

# Eliminar ventaja
@app.route('/admin/advantages/delete/<int:advantage_id>', methods=['POST'])
@login_required
def delete_advantage(advantage_id):
    advantage = Advantage.query.get_or_404(advantage_id)
    db.session.delete(advantage)
    db.session.commit()
    flash('Ventaja eliminada.', 'success')
    return redirect(url_for('admin_advantages'))



# Listar miembros
@app.route('/admin/team')
@login_required
def admin_team():
    members = TeamMember.query.all()
    return render_template('admin_team.html', members=members)

# Añadir miembro
@app.route('/admin/team/add', methods=['GET', 'POST'])
@login_required
def add_team_member():
    form = TeamMemberForm()
    if form.validate_on_submit():
        filename = None
        if form.photo.data:
            filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(app.static_folder, 'images/about', filename))

        member = TeamMember(
            name=form.name.data,
            role=form.role.data,
            description=form.description.data,
            photo_filename=filename
        )
        db.session.add(member)
        db.session.commit()
        flash('Miembro añadido.', 'success')
        return redirect(url_for('admin_team'))
    return render_template('admin_team_form.html', form=form)

# Editar miembro
@app.route('/admin/team/edit/<int:member_id>', methods=['GET', 'POST'])
@login_required
def edit_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    form = TeamMemberForm(obj=member)

    if form.validate_on_submit():
        if form.photo.data:
            if member.photo_filename:
                old_path = os.path.join(app.static_folder, 'images/about', member.photo_filename)
                if os.path.exists(old_path):
                    os.remove(old_path)
            filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(app.static_folder, 'images/about', filename))
            member.photo_filename = filename

        member.name = form.name.data
        member.role = form.role.data
        member.description = form.description.data
        db.session.commit()
        flash('Miembro actualizado.', 'success')
        return redirect(url_for('admin_team'))

    return render_template('admin_team_form.html', form=form, member=member)

# Eliminar miembro
@app.route('/admin/team/delete/<int:member_id>', methods=['POST'])
@login_required
def delete_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    if member.photo_filename:
        path = os.path.join(app.static_folder, 'images/about', member.photo_filename)
        if os.path.exists(path):
            os.remove(path)
    db.session.delete(member)
    db.session.commit()
    flash('Miembro eliminado.', 'success')
    return redirect(url_for('admin_team'))


@app.route('/admin/about', methods=['GET', 'POST'])
@login_required
def admin_about():
    about = About.query.first()
    if not about:
        about = About(title='Sobre Nosotros', paragraph1='', paragraph2='', image_filename=None)
        db.session.add(about)
        db.session.commit()

    form = AboutForm(obj=about)

    if form.validate_on_submit():
        about.title = form.title.data
        about.paragraph1 = form.paragraph1.data
        about.paragraph2 = form.paragraph2.data

        if form.image.data:
            # Borrar imagen anterior si existe
            if about.image_filename:
                old_path = os.path.join(app.static_folder, 'images/about', about.image_filename)
                if os.path.exists(old_path):
                    os.remove(old_path)
            # Guardar nueva imagen
            filename = secure_filename(form.image.data.filename)
            filepath = os.path.join(app.static_folder, 'images/about', filename)
            form.image.data.save(filepath)
            about.image_filename = filename

        db.session.commit()
        flash('Contenido actualizado.', 'success')
        return redirect(url_for('admin_about'))

    features = AboutFeature.query.all()
    return render_template('admin_about.html', form=form, features=features, about=about)

@app.route('/admin/about/feature/add', methods=['GET', 'POST'])
@login_required
def add_about_feature():
    form = AboutFeatureForm()
    if form.validate_on_submit():
        feature = AboutFeature(
            icon=form.icon.data,
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(feature)
        db.session.commit()
        flash('Elemento añadido.', 'success')
        return redirect(url_for('admin_about'))
    return render_template('admin_feature_form.html', form=form)

@app.route('/admin/about/feature/edit/<int:feature_id>', methods=['GET', 'POST'])
@login_required
def edit_about_feature(feature_id):
    feature = AboutFeature.query.get_or_404(feature_id)
    form = AboutFeatureForm(obj=feature)
    if form.validate_on_submit():
        feature.icon = form.icon.data
        feature.title = form.title.data
        feature.description = form.description.data
        db.session.commit()
        flash('Elemento actualizado.', 'success')
        return redirect(url_for('admin_about'))
    return render_template('admin_feature_form.html', form=form)

@app.route('/admin/about/feature/delete/<int:feature_id>', methods=['POST'])
@login_required
def delete_about_feature(feature_id):
    feature = AboutFeature.query.get_or_404(feature_id)
    db.session.delete(feature)
    db.session.commit()
    flash('Elemento eliminado.', 'success')
    return redirect(url_for('admin_about'))




@app.route('/admin/services')
@login_required
def admin_services():
    services = Service.query.all()
    return render_template('admin_services.html', services=services)

@app.route('/admin/services/new', methods=['GET', 'POST'])
@login_required
def new_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(
            title=form.title.data,
            description=form.description.data,
            icon=form.icon.data
        )
        db.session.add(service)
        db.session.commit()
        flash('Servicio creado correctamente.', 'success')
        return redirect(url_for('admin_services'))
    return render_template('service_form.html', form=form, title='Nuevo Servicio')

@app.route('/admin/services/edit/<int:service_id>', methods=['GET', 'POST'])
@login_required
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    form = ServiceForm(obj=service)
    if form.validate_on_submit():
        service.title = form.title.data
        service.description = form.description.data
        service.icon = form.icon.data
        db.session.commit()
        flash('Servicio actualizado.', 'success')
        return redirect(url_for('admin_services'))
    return render_template('service_form.html', form=form, title='Editar Servicio')

@app.route('/admin/services/delete/<int:service_id>', methods=['POST'])
@login_required
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    flash('Servicio eliminado.', 'info')
    return redirect(url_for('admin_services'))

@app.route('/galeria/album/<int:album_id>')
def album_detail(album_id):
    album = Album.query.get_or_404(album_id)
    return render_template('album_detail.html', album=album)

@app.route('/admin/upload', methods=['GET', 'POST'])
@login_required
def upload_image():
    form = ImageUploadForm()
    form.album.choices = [(a.id, a.name) for a in Album.query.all()]

    if form.validate_on_submit():
        files = request.files.getlist(form.images.name)
        saved = 0

        for file in files:
            if file:
                # Aquí generas un nombre único
                filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"

                save_path = os.path.join(app.static_folder, 'images/galeria', filename)
                file.save(save_path)

                new_image = GalleryImage(filename=filename, album_id=form.album.data)
                db.session.add(new_image)
                saved += 1

        db.session.commit()
        flash(f'{saved} imagen(es) subidas correctamente.', 'success')
        return redirect(url_for('galeria'))

    return render_template('upload_image.html', form=form)

@app.route('/admin/delete_image/<int:image_id>', methods=['POST'])
@login_required
def delete_image(image_id):
    image = GalleryImage.query.get_or_404(image_id)

    # Eliminar archivo físico
    file_path = os.path.join(app.static_folder, 'galeria', image.filename)
    if os.path.exists(file_path):
        os.remove(file_path)

    # Eliminar de la base de datos
    db.session.delete(image)
    db.session.commit()

    flash('Imagen eliminada correctamente.', 'success')
    return redirect(request.referrer or url_for('galeria'))


@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg_db = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(msg_db)
        db.session.commit()
        msg = Message('Nuevo mensaje de contacto',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"""
        Nombre: {form.name.data}
        Email: {form.email.data}
        Mensaje: {form.message.data}
        """
        mail.send(msg)
        flash('Tu mensaje ha sido enviado. Gracias por contactarnos.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Bienvenido, has iniciado sesión.', 'success')
            return redirect(url_for('upload_image'))
        else:
            flash('Credenciales incorrectas.', 'danger')
    return render_template('admin_login.html', form=form)

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Crear álbumes si no existen
        # Crear álbumes si no existen
        if Album.query.count() == 0:
            album1 = Album(name="Eventos Corporativos", description="Muestras de eventos empresariales")
            album2 = Album(name="Eventos Sociales", description="Celebraciones sociales y familiares")
            db.session.add_all([album1, album2])
            db.session.commit()

            # Precargar imágenes
            test_images = [
                GalleryImage(filename="evento1.jpg", album_id=album1.id),
                GalleryImage(filename="evento2.jpg", album_id=album1.id),
                GalleryImage(filename="social1.jpg", album_id=album2.id),
                GalleryImage(filename="social2.jpg", album_id=album2.id)
            ]

            db.session.add_all(test_images)
            db.session.commit()

        # Crear usuario admin si no existe
        if not User.query.filter_by(username='jodamu').first():
            from werkzeug.security import generate_password_hash
            hashed_password = generate_password_hash('Twingofhb117@')
            new_user = User(username='jodamu', password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

    app.run(debug=True)
