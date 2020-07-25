# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:54:17 2020

@author: chakanc
"""
import datetime
import jwt
import sys
import sqlite3
from datetime import date
from flask import Flask, request, redirect, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
app.secret_key = 'AABBCCDDEE'
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World 112'

#%%
@app.route('/login', methods=['POST', 'GET'])
def login():
    
    # return render_template('login.html')
    validuser = False
    if request.method == 'GET':
        user = request.args.get('uid')
        print(user)
        if (user == None):
            return render_template('login.html', loginstatus='NA')
        else:
            return render_template('login.html', loginstatus='Alreday Logged in')
    elif request.method == 'POST':
        user = request.form['uid']
        pwd = request.form['pwd']
        print(user)
        #check against DB if valid user
        validuser=False
        try:
                con = sqlite3.connect('PredictorDB.db')
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute('Select username, password from Users where username=? and password = ?', (user, pwd))
                #cur.execute('Select username, password from Users')
                rows = cur.fetchall()
                print ('record fetched successfully')
                for row in rows:
                    validuser=True
                    break
                print('check')
        except:
            con.rollback()
            print ('Unexpected error:', sys.exc_info()[0])
        finally:
            con.close()
            print('finally')
    
        if validuser:
            # if 'username' in session:
            #     user = session["username"]
            # else:
            #     session["username"] = user
            
            session["username"] = encodetoken(user)
            # return redirect(url_for('GetAll', name=user))
            return redirect(url_for('loaddashboard'))
        else:
            return render_template('login.html', loginstatus=validuser)
                

@app.route('/logout')
def logout():
    #session.pop('username', None)
    # for key in session.keys():
    #     session.pop(key, None)
    session.pop('username', None)
    return redirect(url_for('hello_world'))

@app.route('/dashboard')
def loaddashboard():
    user = session['username']
    print(user)
    auser = decodetoken(user)
    print(auser)
    return render_template('Dashboard.html', username=auser)
    
@app.route('/registeruser', methods=['POST', 'GET'])
def registeruser():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        
        username = request.form['uid']
        pwd = request.form['pwd1']
        try:
            with sqlite3.connect('PredictorDB.db') as con:
                cur = con.cursor()
                cur.execute('Insert into Users (username, password, CreatedDate) values (?,?,?)', (username, pwd, date.today()))
                con.commit()
                print ('record enteretd successfully')
        except:
            con.rollback()
            print ('error rolled back')
            print ('Unexpected error:', sys.exc_info()[0])
        finally:
            con.close()
            print ('Connection closed')
            
        return render_template('login.html')

@app.route('/predictsalary', methods=['GET', 'POST'])
def PredictSalary():
    import requests
    user = session["username"]
    if request.method == 'GET':
        return render_template('SalaryPrediction.html', username=user)
    elif request.method == 'POST':
        yoe = request.form['yoe']
        #yoe = '3.2'
        url = 'http://localhost:82/todo/api/v1.0/salarypredictor/' + yoe
        resp = requests.get(url)
        salary = json.loads(resp.text)['salary']
        print(salary)
        return render_template('SalaryPrediction.html', username=user, 
                           predictedsalary=salary)
    
    
@app.route('/getall')
def GetAll():
    dict = {'phy':50,'che':60,'maths':70}
    print(session["username"])
    user = session["username"]
    print(user)
    return render_template('GetAllData.html', results = dict, username=user) 

@app.route('/get/<id>') 
def Get(id):
    return 'Get Data for %s' % id 

@app.route('/delete/<int:id>') # converter types string, int, float, path, uuid
def Delete(id):
    return 'Delete Data for %s' % id 

@app.route('/add/')
def Add():
    return 'Add Data' 


def hello_flask():
    return 'Hello Flask'

app.add_url_rule('/','hello', hello_flask())

#app.run()


def encodetoken(user_id):
    try:
        payload = {
                'exp':datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
        app.config.from_object('config')
        token =  jwt.encode(payload, 
                          app.config.get('SECRET_KEY'),
                          algorithm='HS256'
                          )  
        payload1 = jwt.decode(token, 
                             app.config.get('SECRET_KEY'), 
                             algorithm='HS256')
        print(payload1)
        return token
    except Exception as e:
        return e
def decodetoken(token):
    import sys
    try:
        # token = request.form['token']
        print(token)
        app.config.from_object('config')
        # print(app.config)
        payload = jwt.decode(token, 
                             app.config.get('SECRET_KEY'), 
                             algorithm='HS256')
        print(payload)
        return payload['sub']
    # except jwt.ExpiredSignatureError as e:
    #     return e
    # except jwt.InvalidTokenError as e:
    #     return "Invalid error "
    except:
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])


class TokenManager:
   
    @staticmethod
    def encodetoken(user_id):
        try:
            payload = {
                    'exp':datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                    'iat': datetime.datetime.utcnow(),
                    'sub': user_id
                }
            app.config.from_object('config')
            token =  jwt.encode(payload, 
                              app.config.get('SECRET_KEY'),
                              algorithm='HS256'
                              )  
            payload1 = jwt.decode(token, 
                                 app.config.get('SECRET_KEY'), 
                                 algorithm='HS256')
            print(payload1)
            return payload1['sub']
        except Exception as e:
            return e
    
    @staticmethod
    def decodetoken(token):
        import sys
        try:
            # token = request.form['token']
            print(token)
            app.config.from_object('config')
            # print(app.config)
            payload = jwt.decode(token, 
                                 app.config.get('SECRET_KEY'), 
                                 algorithm='HS256')
            # print(payload)
            return payload['sub']
        # except jwt.ExpiredSignatureError as e:
        #     return e
        # except jwt.InvalidTokenError as e:
        #     return "Invalid error "
        except:
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
            
            
if __name__ == '__main__':
    app.run('localhost',port='81')