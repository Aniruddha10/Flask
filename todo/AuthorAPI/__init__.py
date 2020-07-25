#
from flask import request, jsonify, json
import sys
import initapp, models

app = initapp.getapp(__name__)
db = initapp.getdb(app)

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
     existing_user = models.Author.query.all()
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
        db.session.add(models.Author(name=name))
        db.session.commit()
    except:
        print(sys.exc_info()[2])
    finally:
        print('closed')
    
    return jsonify({'status': 'success'})

def addbook():
    name = request.form['name']
    genre = request.form['book']
    db.session.add(models.Book(name, genre))
 
print(app.config)
durl=app.config["APPURL"]
dport=app.config["PORT"]
app.run(durl, port=dport)
#app.run('localhost', '100')