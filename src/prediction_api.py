import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger
import numpy as np
import pandas as pd
import redis

with open('../models/rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/predict')
def predict_iris():

    """Predicting Bike Demand
    ---
    parameters:
      - name: season
        in: query
        type: number
        required: true
      - name: holiday
        in: query
        type: number
        required: true
      - name: workingday
        in: query
        type: number
        required: true
      - name: weather
        in: query
        type: number
        required: true
      - name: temp
        in: query
        type: number
        required: true
      - name: humidity
        in: query
        type: number
        required: true
      - name: windspeed
        in: query
        type: number
        required: true
      - name: hour
        in: query
        type: number
        required: true
      - name: year
        in: query
        type: number
        required: true
      - name: weekday
        in: query
        type: number
        required: true
      - name: month
        in: query
        type: number
        required: true
    responses:
      200:
        description: Index of predicted class 
    """

    variable_list = ['season', 'holiday', 'workingday', 'weather', 'temp',
       'humidity', 'windspeed', 'hour', 'year', 'weekday', 'month']
    

    request_list = [float(request.args.get(variable)) for variable in variable_list]

    print(np.array(request_list))
    print(np.array(request_list).shape)

    print("Predicting!")
    prediction = model.predict(np.array(request_list).reshape(1, -1))
    # print(prediction)

    print("Returning Prediction")
    return str(prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)