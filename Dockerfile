# Pull base image
FROM python:3.9

# Set work directory
WORKDIR /code/app

# Install dependencies
# syntax: COPY <src relative to dockerfile> <des>
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy project
COPY ./app/main.py /code/app/
COPY ./app/Telco.py /code/app/

COPY ./saved_items /code/saved_items/
COPY ./saved_items/classifier.pkl /code/saved_items/
COPY ./saved_items/scaler.pkl /code/saved_items/


# run command prompt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]