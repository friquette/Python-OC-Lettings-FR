FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /django-app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
