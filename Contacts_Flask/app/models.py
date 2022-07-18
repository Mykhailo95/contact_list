from sqlalchemy import ForeignKey
from . import db

class Phone(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.Integer, index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

class Email(db.Model):
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), index=True, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(24), index=True,  nullable=False)
    age = db.Column(db.Integer)
    favorit = db.Column(db.Boolean, default=False)
    phone_id = db.Column(db.Integer, ForeignKey('phone.id'))
    email_id = db.Column(db.Integer, ForeignKey('email.id'))

    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'User {self.username}'