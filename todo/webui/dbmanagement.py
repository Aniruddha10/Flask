# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:27:31 2020

@author: chakanc
"""

import sqlite3

conn = sqlite3.connect('PredictorDB.db')

# print ('Opened database successfully')
# conn.execute('Create Table Users (username Text, password Text, CreatedDate DateTime)')
# print ('Table Created successfully')

# print ('Opened database successfully')
# conn.execute('Create Table Tasks (taskid int, title Text, description Text, status boolean)')
# print ('Table Created successfully')

conn.close()