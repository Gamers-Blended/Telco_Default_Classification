# import package
from pydantic import BaseModel


# Class which describles telco data (name and dtypes)
class Telco(BaseModel):
	tenure: int
	InternetService_Fiber_optic: int
	InternetService_No: int
	Contract_Month_to_month: int
	Contract_Two_year: int
	PaymentMethod_Electronic_check: int