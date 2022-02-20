FROM python:3.9

WORKDIR /code/app

COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app/main.py /code/app/

COPY ./app/Telco.py /code/app/

COPY ./saved_items /code/saved_items/
COPY ./saved_items/classifier.pkl /code/saved_items/
COPY ./saved_items/scaler.pkl /code/saved_items/





CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]