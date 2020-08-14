import numpy as np
import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier

class ModelBuilder:

    def __init__(self):
        self.df = pd.read_csv('ModelBuilder/data/data.csv')
        try:
            self.model = joblib.load('models/trained.model')
        except:
            self.model = None
        
    def fit(self):
        X = self.df.drop('target', axis=1)
        y = self.df['target']
        
        self.model = RandomForestClassifier(max_depth=5).fit(X, y)
        joblib.dump(self.model, 'models/trained.model')
        print('='*50)
        print('Finished Training')
        print('='*50)
        
    def predict(self, inputs):
        print('predict')
        if not os.path.isfile('models/trained.models'):
            print('PLEASE TRAIN THE MODEL FIRST BEFORE RUNNING A PREDICTION.')
        elif len(inputs) != len(self.df.drop('target', axis=1).columns):
            print('Missing Input.')

        return self.model.predict([inputs])
        print('PREDICTION PROCESS IS SUCCESSFUL.')