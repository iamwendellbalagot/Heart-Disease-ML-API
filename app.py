import numpy as np
import pandas as pd
import os
import joblib

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
from ModelBuilder.ModelBuilder import ModelBuilder
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)



class Predict(Resource):
    @staticmethod
    def post():
        model = ModelBuilder()
        data = request.get_json()
        params = []
        
        for val in data.values():
            params.append(val)
        if not os.path.isfile('models/trained.model'):
            model.fit()
        else:
            prediction, proba =  model.predict(params)
            proba = round(proba.flatten().max()*100,2)
            print(data)
            if prediction == 0:
                return jsonify( {'input': data,
                                 'prediction': 'No',
                                 'probability':proba})
                print(prediction)
            else:
                return jsonify({'input': data, 
                                'prediction': 'Yes',
                                'probability':proba})
                print(prediction)
                
api.add_resource(Predict, '/testapi')

if __name__ == '__main__':
    app.run(debug=True)