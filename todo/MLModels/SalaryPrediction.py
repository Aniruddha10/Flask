# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:19:14 2020

@author: chakanc
"""

from sklearn import linear_model
import matplotlib.pyplot as mp
import numpy as np

#regressor = ""

#train SLR model on Training set
def trainModel(X_train, y_train):
    #print(X_train)
    #print(y_train)
    regressor = linear_model.LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor        

def showTheta(regressor):
    print('Coefficient {} '.format(regressor.Coefficient))

#Predict test Set
def predictTest(regressor, X_test):
    y_test = regressor.predict(X_test)
    np.set_printoptions(precision=2)
    return y_test

def predictMultiTest(regressor, X_test, y_test):
    y_pred = regressor.predict(X_test)
    np.set_printoptions(precision=2)
    
    y_pred_array = y_pred.reshape(len(y_pred), 1)
    
    y_test_nparray = np.array(y_test)
    y_test_array = y_test_nparray.reshape(len(y_test_nparray),1)
    
    print(np.concatenate((y_pred_array, y_test_array), 1))
    return y_test
            
#Visualize training set results
def drawTrainSet(X_train, y_train):
    mp.scatter(X_train, y_train, color='black')
    mp.plot(X_train, y_train, color = 'blue', linewidth=3)

#Visualize Test set results
def drawTestSet(X_test, y_test):
    mp.scatter(X_test, y_test, color='black')
    #mp.plot(X_test, y_test, color = 'blue', linewidth=1)
    mp.show()