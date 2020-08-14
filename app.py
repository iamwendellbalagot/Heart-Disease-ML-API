import numpy as np
import pandas as pd
import os
import joblib

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
from ModelBuilder.ModelBuilder import ModelBuilder

app = Flask(__name__)
api = Api(app)



class Predict(Resource):
    @staticmethod
    def post():
        model = ModelBuilder()
        data = request.get_json()
        params = []
        
        for val in data.values():
            params.append(val)
        print(params)
        if not os.path.isfile('models/trained.model'):
            model.fit()
        else:
            prediction =  model.predict(params)
            print(prediction)
            if prediction == 0:
                return jsonify( {'Input': data,'Prediction: ': 'NO HEART DISEASE'})
                print(prediction)
            else:
                return jsonify({'Input': data, 'Prediction': 'YOU HAVE HEART DISEASE'})
                print(prediction)
                
api.add_resource(Predict, '/')

if __name__ == '__main__':
    app.run(debug=True)