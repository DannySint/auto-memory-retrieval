# FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# COPY ocr/requirements.txt /code/
# WORKDIR /code
# RUN pip install -r requirements.txt
# COPY . /code/

FROM node:latest

COPY web/package.json .
RUN npm install --quiet

COPY ./web .
EXPOSE 3000