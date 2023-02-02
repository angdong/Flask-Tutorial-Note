# Database Model 정의 -> User/Note에 대한 데이터를 정의할 예정
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    # id, email, password, nickname
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    notes = db.relationship('Note')

class Note(db.Model):
    # id, title, content, datetime
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(2000))
    datetime = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))