# import package
from pydantic import BaseModel


# Class which describles telco data (name and dtypes)
class Telco(BaseModel):
	gender: int
	SeniorCitizen: int
	Partner: int
	Dependents: int
	tenure: float
	PhoneService: int
	MultipleLines: int
	OnlineSecurity: int
	OnlineBackup: int
	DeviceProtection: int
	TechSupport: int
	StreamingTV: int
	StreamingMovies: int
	PaperlessBilling: int
	MonthlyCharges: float
	TotalCharges: float
	InternetService_DSL: int
	InternetService_Fiber_optic: int
	InternetService_No: int
	Contract_Month_to_month: int
	Contract_One_year: int
	Contract_Two_year: int
	PaymentMethod_Bank_transfer_automatic: int
	PaymentMethod_Credit_card_automatic: int
	PaymentMethod_Electronic_check: int
	PaymentMethod_Mailed_check: int