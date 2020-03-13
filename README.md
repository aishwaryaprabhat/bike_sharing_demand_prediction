# Forecasting Demand for Bike Sharing

![](https://cdn.dribbble.com/users/449626/screenshots/3679748/bike_sharing.gif)

Prediction API available at: http://bike-pred.herokuapp.com/apidocs/

## Purpose of this Repository

This repository serves primarily as source material for Aish's NUS guest lecture 'Machine Learning in the Real World' for Masters students in IE5105 Modeling for Supply Chain Systems course. The repo can be used as a tutorial to go through the following 8 step process to take a Machine Learning model from proof-of-concept to production:

1. Frame the problem and look at the big picture.
2. Get the data.
3. Explore the data to gain insights.
4. Prepare the data to better expose the underlying data patterns to Machine Learning
algorithms.
5. Explore many different models and short-list the best ones.
6. Fine-tune your models and combine them into a great solution.
7. Build an API using Flask and Swagger
8. Launch, monitor, and maintain your system using Docker and Kubernetes/Heroku


## Lecture Objectives

1. Share a simplified version of a typical process of developing a Machine Learning solution
2. Share some of the techniques, algorithms, technologies involved
3. Share key things to keep in mind when developing a Machine Learning solution


## How to run the project

### EDA & Model Development

- For EDA run `model-training/ Bike Sharing EDA.ipynb`
- For feature engineering and model development run `model-training/Feature Engineering & Model Development.ipynb`

### API Development
- For a simple Flask+Swagger API script take a look at `api/prediction_api.py`

```
import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger
import numpy as np
import os 


with open('../models/rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
swagger = Swagger(app)

port = int(os.environ.get("PORT", 5000))

@app.route('/')
def landing_page():

  return "Go to https://bike-pred.herokuapp.com/apidocs", 200

@app.route('/predict')
def predict_bike_demand():
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
    app.run(host='0.0.0.0', port=port)
    
```


### Containerization (using Docker)

- We build a simple and lean docker image using `Dockerfile`

```
  
FROM python:3.6
MAINTAINER aish, aish.prabhat@shopee.com
COPY requirements.txt bike/
WORKDIR bike/
RUN pip install -r requirements.txt
COPY ./models ./models
COPY ./api ./api
WORKDIR api/
EXPOSE 5000
CMD gunicorn wsgi:app

```
- Run the following command 
`docker build -t bike .`

### Container Orchstration/Hosting using Heroku

```
heroku create <app-name>
heroku container:push web --app <app-name>
heroku container:release web --app <app-name>
```

## Important Links
1. [Web App](http://bike-pred.herokuapp.com/apidocs/)
1. [Awesome Online Machine Learning Course](https://www.udemy.com/course/machinelearning/)
1. [Awesome book on Machine Learning](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291)
1. [Free YouTube Machine Learning Tutorial](https://pythonprogramming.net/machine-learning-tutorial-python-introduction/)
1. [Aish's Website](https://www.aishwaryaprabhat.com/)
1. [Aish's blog](https://medium.com/@aishwaryaprabhat)
1. [Aish's Linkedin](https://www.linkedin.com/in/aishwaryaprabhat/)



