from fastapi.testclient import TestClient
from app import app

# Create a TestClient passing to it the FastAPI application
client = TestClient(app)


def test_read_main():
    # response = client.get("/1,0,0,0,10.5,0,0,1,0,0,0,0,0,0,23.5,50.50,1,0,0,0,0,1,0,1,0,0")
    response = client.get("/name")

    # Write simple assert statements with the standard Python expressions that need to check
    assert response.status_code == 200
    # try:
    assert response.json() == {"Welcome To The Telco Default Classifier": "name"}

    assert response.status_code == 200
    assert response.json() == {"prediction": "No, customer unlikely to default payment"}
    assert response.json() == {"prediction": "Yes, customer is likely to default on payment"}
    # except AssertionError as msg:
        # print(msg)


def dummy_customer():
    customer= {'PassengerId': 2,
                  'gender': 1,
    'SeniorCitizen': 0,
    'Partner': 0,
    'Dependents': 1,
    'tenure': 23.5,
    'PhoneService': 0,
    'MultipleLines': 0,
    'OnlineSecurity': 0,
    'OnlineBackup': 0,
    'DeviceProtection': 0,
    'TechSupport': 0,
    'StreamingTV': 0,
    'StreamingMovies': 0,
    'PaperlessBilling': 1,
    'MonthlyCharges': 12.30,
    'TotalCharges': 130.50,
    'InternetService_DSL': 0,
    'InternetService_Fiber_optic': 1,
    'InternetService_No': 0,
    'Contract_Month_to_month': 0,
    'Contract_One_year': 1,
    'Contract_Two_year': 0,
    'PaymentMethod_Bank_transfer_automatic': 0,
    'PaymentMethod_Credit_card_automatic': 1,
    'PaymentMethod_Electronic_check': 0,
    'PaymentMethod_Mailed_check': 0}

    return passenger2

def test_dt_invariance(dummy_titanic_dt, dummy_passengers):
    model = dummy_titanic_dt
    _, p2 = dummy_passengers

    # Get original survival probability of passenger 2
    test_df = pd.DataFrame.from_dict([p2], orient='columns')
    X, y = get_feats_and_labels(prep_df(test_df))
    p2_prob = model.predict(X)[0]  # 1.0