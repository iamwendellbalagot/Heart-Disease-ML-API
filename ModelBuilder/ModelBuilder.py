import numpy as np
import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

class ModelBuilder:

    def __init__(self):
        self.df = pd.read_csv('ModelBuilder/data/data.csv')
        try:
            self.model = joblib.load('models/trained.model')
            self.scaler = joblib.load('models/scaler.model')
        except:
            self.model = None
            self.scaler = None
        
    def fit(self):
        #separate the features
        X = self.df.drop('target', axis=1)
        y = self.df.target

        #normalize
        self.scaler = StandardScaler().fit(X)
        X = self.scaler.transform(X)
        
        #hyperparameter tuning
        best_params = {'max_depth': 30,
                       'min_samples_leaf': 5,
                       'min_samples_split': 5,
                       'n_estimators': 500}

        self.model =RandomForestClassifier(**best_params).fit(X, y)
        
        joblib.dump(self.model, 'models/trained.model')
        joblib.dump(self.scaler, 'models/scaler.model')
        print('='*50)
        print('Finished Training')
        print('='*50)
        
    def predict(self, inputs):
        if not os.path.isfile('models/trained.model'):
            print('PLEASE TRAIN THE MODEL FIRST BEFORE RUNNING A PREDICTION.')
        elif len(inputs) != len(self.df.drop('target', axis=1).columns):
            print('Missing Input.')
        inputs = self.scaler.transform([inputs])
        return self.model.predict(inputs), self.model.predict_proba(inputs)
        print('PREDICTION PROCESS IS SUCCESSFUL.')