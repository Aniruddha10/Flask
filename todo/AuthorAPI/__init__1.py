#
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, json
import sys

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///authordb.sqlite3'
db= SQLAlchemy(app)

# class AuthorDB(db.Model):
#     id = db.Column('id', db.Integer, primary_key = True)
    
class Author (db.Model):
    __tablename__ = "Authors"
    id = db.Column('author_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    
    def __init__(self, name):
        self.name = name
        
        
    
class Book (db.Model):
    __tablename__ = "Books"
    id = db.Column('book_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    genre = db.Column(db.String(20))
    
    def __init__(self,name, genre):
        self.name = name
        self.genre = genre

@app.route('/createdb')    
def createdb():
    try:
        db.create_all()
    except:
        print(sys.exc_info()[2])
    finally:
        print('closed')
    
    return jsonify({'status': 'success'})
    
@app.route('/getauthors', methods=['GET'])
def getauthors():
     
    # try:
     # print(jsonify(Author.query.all()))
     # athrs = jsonify(Author.query.all()) 
     # existing_user = Author.query.filter(Author.name == 'Ani1').first()
     existing_user = Author.query.all()
     lst = []
     for i in existing_user:
         lst.append(i.name)
         print(i.id)
         print(i.name)
         
     # ret = jsonify(json_list = [i.serialize for i in existing_user])
     # ret = jsonify({'URS':existing_user})
     if existing_user:
         ret = jsonify(json.dumps(lst))
     else:
         ret = jsonify({'status': 'falied'})
        
     return ret
    # except:
    #     print(sys.exc_info()[2])
    # finally:
    #     print('closed')
    # return jsonify(athrs)
   

@app.route('/addauthor', methods=['POST'])
def addauthor():
    try:
        
        name = request.form['name']
        db.session.add(Author(name=name))
        db.session.commit()
    except:
        print(sys.exc_info()[2])
    finally:
        print('closed')
    
    return jsonify({'status': 'success'})

def addbook():
    name = request.form['name']
    genre = request.form['book']
    db.session.add(Book(name, genre))
    
app.run('localhost', '100')