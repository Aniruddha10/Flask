# -*- coding: utf-8 -*-

import DataPreprocessing as dp
import SalaryPrediction as sp
import numpy as np
import pickle

def SLR():
    print ('call functions SLR')
    
    # Data Preprocessing
    X,y = dp.readData('Salary_Data.csv')
    print(np.array(X))
    print(np.array(y))
    
    X_array = np.array(X)
    
    y_array = np.array(y)
    print(X_array)
    print(y_array)
    np.set_printoptions(2)
    print(np.concatenate((X_array.reshape(len(X_array), 1), 
                    y_array.reshape(len(y_array),1)),1))
    
    m = len(X_array)
    theta0Array = np.ones((m,1))
    print(np.concatenate((theta0Array,X_array),1))    
    
    X_train, y_train, X_test, y_test = dp.splitData(X, y)
    
    #print(X_train)
    #print(y_train)
   # Apply simple linear regression
    regressor = sp.trainModel(X_train, y_train)
    
    #pfilename = 'C:\self\salarypredictor.pkl'
    pfilename = 'salarypredictor.pkl'
    with open(pfilename, 'wb') as file:
        pickle.dump(regressor, file)
    
    # with open(pfilename, 'rb') as file:
    #     regressor = pickle.load(file)
    
    #sp.showTheta()
    #sp.drawTrainSet(X_train, y_train)
    sp.drawTestSet(X_test, sp.predictTest(regressor, X_test))
    
def MSLR():
    print ('call functions MSLR')
    
    # Data Preprocessing
    X,y = dp.readData('50_Startups.csv')
    X = dp.EncodeData(X, 'State')
    X_train, y_train, X_test, y_test = dp.splitData(X, y)
    
    #print(X_train)
    #print(y_train)
   # Apply simple linear regression
    regressor = sp.trainModel(X_train, y_train)
    
    #sp.showTheta()
    #sp.drawTrainSet(X_train, y_train)
    yt=sp.predictMultiTest(regressor, X_test, y_test)
    print(X_test)
    
    print(yt)
    sp.drawTestSet(X_test[:,3], yt)
    
    
def main():
    SLR()
    
main()