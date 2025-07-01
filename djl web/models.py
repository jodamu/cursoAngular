from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255))
    images = db.relationship('GalleryImage', backref='album', lazy=True)

class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    company = db.Column(db.String(150), nullable=True)
    event_type = db.Column(db.String(50), nullable=True)
    event_date = db.Column(db.Date, nullable=True)
    attendees = db.Column(db.Integer, nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(50), nullable=False)  # clase de ícono Bootstrap

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    paragraph1 = db.Column(db.Text, nullable=False)
    paragraph2 = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(255), nullable=True)  # Imagen opcional

class AboutFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)


class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    photo_filename = db.Column(db.String(255), nullable=True)


class Advantage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_filename = db.Column(db.String(255), nullable=True)

class HomeSlide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(255), nullable=True)

class HomeWelcome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    paragraph = db.Column(db.Text, nullable=False)

class HomeFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)


