# -*- coding: utf-8 -*-
import initapp, jsonify, json

app = initapp.getapp(__name__)
db = initapp.getdb(app)

# class AuthorDB(db.Model):
#     id = db.Column('id', db.Integer, primary_key = True)
    

class Author (db.Model):
    __tablename__ = "Authors"
    id = db.Column('author_id', db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(100))
    
    def __init__(self, name):
        self.name = name
        
    
class Book (db.Model):
    __tablename__ = "Books"
    id = db.Column('book_id', db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(100))
    genre = db.Column(db.String(20))
    
    def __init__(self,name, genre):
        self.name = name
        self.genre = genre
