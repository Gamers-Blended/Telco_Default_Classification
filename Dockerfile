FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/
COPY ./classifier.pkl /code/
COPY ./Telco.py /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]