# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from sklearn.linear_model import LinearRegression
import sqlite3, sys, os
from decimal import Decimal
import pickle

app = Flask(__name__, instance_relative_config=True)

#read configuration
try:
    #app.config["SECRET_KEY"] = "iuhto743yto34iuho287gh78"
    
    # Load the default configuration default.py
    app.config.from_object('webapiconfig.default')
    
    # Load the file specific to environment based on ENV variable
    app.config.from_object('webapiconfig.'+ os.getenv('FLASK_ENV'))
    
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')
    
    # Load from json
    # app.config.from_json('webapi/config/default.json')
except :
    print(sys.exc_info()[2])
finally:
    print('config read closed')

@app.route('/todo/api/v1.0/salarypredictor/<yoe>', methods=['GET'])
def predict_salary(yoe):
    filename='salarypredictor.pkl'
    yoe = [[Decimal(yoe)]]
    salary = 0
    regressor = LinearRegression()
    with open(filename, 'rb') as file:
        regressor = pickle.load(file)
        salary = regressor.predict(yoe)
    return jsonify({'salary': salary[0]})

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    tasks = ''
    try:
        con = sqlite3.connect('PredictorDB.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('Select * from Tasks')
        rows = cur.fetchall()
        tasks = rows
    except:
        con.rollback()
        print ('Unexpected error:', sys.exc_info()[0])
    finally:
        con.close()
        print('finally')
    return jsonify({'tasks': tasks})

#read configuration

# FN = app.config["FNLabel"]
print(app.config)
durl=app.config["APPURL"]
dport=app.config["PORT"]
app.run(durl, port=dport)