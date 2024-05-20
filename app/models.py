# from .config import db
from flask_sqlalchemy import SQLAlchemy
# from flask import current_app


db = SQLAlchemy()

class Domains(db.Model):
    __tablename__ = 'domains'
    domain = db.Column(db.String(500), nullable=False)
    subdomain = db.Column(db.String(500), nullable=False, primary_key=True)
    updatetime = db.Column(db.DateTime())
    checkedtime = db.Column(db.Integer)
    ifon = db.Column(db.Integer)
    status = db.Column(db.Integer)

class AddedDomains(db.Model):
    __tablename__ = 'added_domains'
    domain = db.Column(db.String(500), nullable=False)
    subdomain = db.Column(db.String(500), nullable=False, primary_key=True)
    updatetime = db.Column(db.DateTime())
    checkedtime = db.Column(db.Integer)

class DeletedDomains(db.Model):
    __tablename__ = 'deleted_domains'
    domain = db.Column(db.String(500), nullable=False)
    subdomain = db.Column(db.String(500), nullable=False, primary_key=True)
    updatetime = db.Column(db.DateTime())
    checkedtime = db.Column(db.Integer)

class TaskRecord(db.Model):
    domain = db.Column(db.String(500), nullable=False, primary_key=True)
    add_time = db.Column(db.DateTime())
    status = db.Column(db.Integer, default=0)
