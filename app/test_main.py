from fastapi.testclient import TestClient
from main import app, classifier
import random
import pytest
import math
import torch
import numpy as np
import pickle


# Create a TestClient passing to it the FastAPI application
client = TestClient(app)

#-------------------------------------------------------------------
def create_dummy_customer(): # dictionary
    """
    Create a dummy customer input data
    """
    customer = {
    'tenure': 24,
    'InternetService_Fiber_optic': random.randint(0,1),
    'InternetService_No': random.randint(0,1),
    'Contract_Month_to_month': random.randint(0,1),
    'Contract_Two_year': random.randint(0,1),
    'PaymentMethod_Electronic_check': random.randint(0,1)}

    return customer

#-------------------------------------------------------------------
def test_model_return_object():
    """
    Test returned object of model function
    """
    customer = create_dummy_customer()
    inputs = list(customer.values())

    scaler = pickle.load(open('../saved_items/scaler.pkl', 'rb'))
    tenure_input = [[inputs[0]]]
    tenure_input = scaler.transform(tenure_input)
    inputs[0] = tenure_input[0][0]
    inputs = torch.from_numpy(np.asarray(inputs))
    prediction = classifier.predict([inputs])
    
    #=================================
    # TEST SUITE
    #=================================
    # Check return object type
    assert isinstance(prediction, np.ndarray)
    # Check length of returned object
    assert len(prediction) == 1

#-------------------------------------------------------------------
def test_model_return_vals():
    """
    Test for returned values of model function
    """
    customer = create_dummy_customer()
    inputs = list(customer.values())

    scaler = pickle.load(open('../saved_items/scaler.pkl', 'rb'))
    tenure_input = [[inputs[0]]]
    tenure_input = scaler.transform(tenure_input)
    inputs[0] = tenure_input[0][0]
    inputs = torch.from_numpy(np.asarray(inputs))
    prediction = classifier.predict([inputs])
    
    #=================================
    # TEST SUITE
    #=================================
    # Check returned prediction type
    assert isinstance(prediction[0], np.int64)
    # Check output contains correct values 0 or 1
    assert 0 in prediction or 1 in prediction

#-------------------------------------------------------------------

def test_raised_exception():
    """
    Tests for raised exception with pytest.raises context manager
    """
    # ValueError
    with pytest.raises(ValueError) as exception:
        customer = create_dummy_customer() 
        inputs = list(customer.values())
        # insert a np.nan randomly into 1 of the elements
        n = len(inputs)
        random_idx = random.randint(0,n-1)
        inputs[random_idx] = np.nan
        
        # if tenure is not nan, normalise it, else skip
        if not math.isnan(inputs[0]):
            scaler = pickle.load(open('../saved_items/scaler.pkl', 'rb'))
            tenure_input = [[inputs[0]]]
            tenure_input = scaler.transform(tenure_input)
            inputs[0] = tenure_input[0][0]

        inputs = torch.from_numpy(np.asarray(inputs))
        prediction = classifier.predict(inputs)
        assert "there is a missing value" in str(exception.value)
    

# Check Enum method for checking of dtypes