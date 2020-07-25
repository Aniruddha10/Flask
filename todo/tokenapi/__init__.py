#
from flask import Flask, request
import datetime
import jwt

app = Flask(__name__)

@app.route('/token/api/encodetoken/<user_id>', methods=['GET'])
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

@app.route('/token/api/decodetoken/<token>', methods=['GET'])
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
        
app.run('localhost', '83')