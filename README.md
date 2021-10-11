# Work in progress
# Telco_Default_Classification
Code for training TabNet classification model and deploying it on FastAPI

## Instructions
1. Clone this repo
2. Open up the command prompt
3. Change the directory to the root of the cloned repo - the directory should contain the `Dockerfile` and `app` folder
4. Ensure Docker is running in your local system
5. Run the following command in the command prompt to build the FastAPI image: <br>
`docker build -t myimage .`

6. Once the image has been built, run a container based on the image by running the following command in the command prompt: <br>
`docker run -d --name mycontainer -p 80:80 myimage`
7. Open a web broswer
8. Head to http://127.0.0.1:8000/docs
9. Under POST, click on "Try it out"
10. These are the required inputs the model takes to make a prediction:
` {
  "gender": 0,
  "SeniorCitizen": 0,
  "Partner": 0,
  "Dependents": 0,
  "tenure": 0,
  "PhoneService": 0,
  "MultipleLines": 0,
  "OnlineSecurity": 0,
  "OnlineBackup": 0,
  "DeviceProtection": 0,
  "TechSupport": 0,
  "StreamingTV": 0,
  "StreamingMovies": 0,
  "PaperlessBilling": 0,
  "MonthlyCharges": 0,
  "TotalCharges": 0,
  "InternetService_DSL": 0,
  "InternetService_Fiber_optic": 0,
  "InternetService_No": 0,
  "Contract_Month_to_month": 0,
  "Contract_One_year": 0,
  "Contract_Two_year": 0,
  "PaymentMethod_Bank_transfer_automatic": 0,
  "PaymentMethod_Credit_card_automatic": 0,
  "PaymentMethod_Electronic_check": 0,
  "PaymentMethod_Mailed_check": 0
}
`
11. Once the values are added, click the "Execute" button to run the model
12. The model will give its prediction under **Server response**
