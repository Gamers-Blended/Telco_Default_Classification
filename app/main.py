# Import library
import uvicorn
from fastapi import FastAPI
from Telco import Telco

# additional packages needed
import torch
import numpy as np
import pickle


# create app object
app = FastAPI(title="Telco Payment Default Predictor")
# load up the predictive model
pickle_in = open("../saved_items/classifier.pkl","rb")
classifier=pickle.load(pickle_in)


# index route
# opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Welcome to the Telco Default API'}


# expose prediction functionality
# make prediction from passed JSON data
@app.post('/predict')
def predict_default(data:Telco):
    data = data.dict()
    tenure=data['tenure']
    InternetService_Fiber_optic=data['InternetService_Fiber_optic']
    InternetService_No=data['InternetService_No']
    Contract_Month_to_month=data['Contract_Month_to_month']
    Contract_Two_year=data['Contract_Two_year']
    PaymentMethod_Electronic_check=data['PaymentMethod_Electronic_check']

    inputs = [tenure,
            InternetService_Fiber_optic,
            InternetService_No,
            Contract_Month_to_month,
            Contract_Two_year,
            PaymentMethod_Electronic_check]

    # normalise tenure with same scalar used for train set
    scaler = pickle.load(open('../saved_items/scaler.pkl', 'rb'))
    # get single input of tenure and convert it as a 2D array
    tenure_input = [[inputs[0]]]
    # normalise input
    tenure_input = scaler.transform(tenure_input)
    # replace raw tenure with normalised tenure
    inputs[0] = tenure_input[0][0]

    # convert input array into numpy array for model to read
    inputs = torch.from_numpy(np.asarray(inputs))

    # make prediction
    prediction = classifier.predict([inputs])
    # predicted class with the highest probability
    highest_proba = max(classifier.predict_proba([inputs]).tolist()[0])

    # 1 = Yes, 0 = No
    # convert result into a readable format
    if(prediction[0] == 1):
        prediction = "YES, customer is likely to default on payment"
    else:
        prediction = "NO, customer unlikely to default payment"
    return {
        'prediction': prediction,
        'probability': "%.2f" % highest_proba + "%"
    }

# run API with uvicorn
# on http://127.0.0.1:8000
# open http://127.0.0.1:8000/docs
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# run this command in cmd
# uvicorn main:app --reload

# syntax:
# {file name}: {object name}
# --reload allows the command to be re-run automatically upon every update of this file