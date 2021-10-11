# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Telco import Telco
import numpy as np
import pandas as pd
import pickle

# 2. Create app object
app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get("/")
async def read_main():
	return {"Hello": "World"}

# 4. Route with single parameter, returns parameter within a message
# Located at: http://127.0.0.1:8000/AnyNameHere
