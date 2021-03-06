# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#COPY . /code/

COPY . .

RUN pip install -U pip && \
   pip install poetry && \
   poetry config virtualenvs.create false && \
   poetry install --no-dev