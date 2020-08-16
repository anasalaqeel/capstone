import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = 'postgres://postgres:1234@localhost:5432/capstone'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    

class Movies(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), nullable=False)
    release_date = Column(String(80), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Actors(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()