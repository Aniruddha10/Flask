# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db= SQLAlchemy(app)

class dbcontext:
   def __init__(self, app):
      self.app = app
      self.db= SQLAlchemy(app)
    
   def createdb(self):
      self.db.create_all()
    
class AuthorDB(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    
class Author (AuthorDB):
    name = db.Column(db.String(100))
    
    def __init__(self, name):
        self.name = name
    
class Book (AuthorDB):
    name = db.Column(db.String(100))
    genre = db.Column(db.String(20))