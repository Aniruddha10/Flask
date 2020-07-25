# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def getapp(appname):
    app = Flask(appname)
    # apply configuration

    # configure dev database    
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///authordb.sqlite3'

    app.config.from_object('config.development')
    return app

def getdb(app):
    db= SQLAlchemy(app)
    return db