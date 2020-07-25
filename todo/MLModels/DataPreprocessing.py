# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:24:44 2020

@author: chakanc
"""

from pandas import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

dataset = ""


#Encoding - One Hot
def EncodeData(X, column):
    cat_features = [column]
    ct = ColumnTransformer(transformers=[('enc1', OneHotEncoder(), cat_features)], 
                           remainder='passthrough')
    X = ct.fit_transform(X)
    return X
    
#split into trainig and test set
def splitData(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1)
    return X_train, y_train, X_test, y_test

#read data
def readData(filename):
    if filename == "":
        raise FileNotFoundError("File not found")
    try:
        dataset = pd.read_csv(filename)
        X = dataset.iloc[:,:-1]
        y = dataset.iloc[:,-1]
    except:
        print("error")
        #throw to thecaller
    finally:
        return X,y
        print("complete")

    