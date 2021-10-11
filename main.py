# Import library
import uvicorn
from fastapi import FastAPI
from Telco import Telco

# additional packages needed
import torch
import numpy as np
import pickle


# create app object
app = FastAPI()
# load up the predictive model
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


# index route
# opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello World'}


# route with single parameter
# returns parameter within a message located at:
# http://127.0.0.1:8000/{name}
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To The Telco Default Classifier': f'{name}'}


# expose prediction functionality
# make prediction from passed JSON data
# return predicted default outcome (y/n)
@app.post('/predict')
def predict_default(data:Telco):
    data = data.dict()
    gender=data['gender']
    SeniorCitizen=data['SeniorCitizen']
    Partner=data['Partner']
    Dependents=data['Dependents']
    tenure=data['tenure']
    PhoneService=data['PhoneService']
    MultipleLines=data['MultipleLines']
    OnlineSecurity=data['OnlineSecurity']
    OnlineBackup=data['OnlineBackup']
    DeviceProtection=data['DeviceProtection']
    TechSupport=data['TechSupport']
    StreamingTV=data['StreamingTV']
    StreamingMovies=data['StreamingMovies']
    PaperlessBilling=data['PaperlessBilling']
    MonthlyCharges=data['MonthlyCharges']
    TotalCharges=data['TotalCharges']
    InternetService_DSL=data['InternetService_DSL']
    InternetService_Fiber_optic=data['InternetService_Fiber_optic']
    InternetService_No=data['InternetService_No']
    Contract_Month_to_month=data['Contract_Month_to_month']
    Contract_One_year=data['Contract_One_year']
    Contract_Two_year=data['Contract_Two_year']
    PaymentMethod_Bank_transfer_automatic=data['PaymentMethod_Bank_transfer_automatic']
    PaymentMethod_Credit_card_automatic=data['PaymentMethod_Credit_card_automatic']
    PaymentMethod_Electronic_check=data['PaymentMethod_Electronic_check']
    PaymentMethod_Mailed_check=data['PaymentMethod_Mailed_check']
  
    inputs = [gender,SeniorCitizen,Partner,Dependents,tenure,
        PhoneService,MultipleLines, OnlineSecurity, OnlineBackup,
       DeviceProtection,TechSupport,StreamingTV, StreamingMovies,
       PaperlessBilling,MonthlyCharges,TotalCharges,
       InternetService_DSL,InternetService_Fiber_optic,
       InternetService_No,Contract_Month_to_month,Contract_One_year,
       Contract_Two_year, PaymentMethod_Bank_transfer_automatic,
       PaymentMethod_Credit_card_automatic,
       PaymentMethod_Electronic_check, PaymentMethod_Mailed_check]

    # convert input array into numpy array for model to read
    inputs = torch.from_numpy(np.asarray(inputs))

    # make prediction
    prediction = classifier.predict([inputs])
    # 1 = Yes, 0 = No
    if(prediction[0] == 1):
        prediction = "Yes, customer is likely to default on payment"
    else:
        prediction = "No, customer unlikely to default payment"
    return {
        'prediction': prediction
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