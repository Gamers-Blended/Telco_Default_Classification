# 1. Library imports
import uvicorn
from fastapi import FastAPI
import torch
from Telco import Telco
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To The Telco Default Classifier': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted default outcome
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

    inputs = torch.from_numpy(np.asarray(inputs))


    prediction = classifier.predict([inputs])
    if(prediction[0]>0.5):
        prediction="Yes, customer is likely to default on payment"
    else:
        prediction="No, customer unlikely to default payment"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# file name: object name
#uvicorn app:app --reload