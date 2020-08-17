import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = 'postgres://zfckaisbrimmqr:b0a237b5797ef97a432179491bac2930931136c681c536c0c71f3c028685127f@ec2-35-175-155-248.compute-1.amazonaws.com:5432/d9pop022tk93e1'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    """
    drops the database tables and starts fresh
    can be used to initialize a clean database
    """
    db.drop_all()
    db.create_all()
    

class Movies(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), nullable=False)
    release_date = Column(Integer(), nullable=False)

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