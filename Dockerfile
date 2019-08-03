# FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# COPY ocr/requirements.txt /code/
# WORKDIR /code
# RUN pip install -r requirements.txt
# COPY . /code/

FROM node:10
WORKDIR /app
COPY web/package.json package.json
RUN npm install
COPY . .
EXPOSE 3000
RUN npm install -g nodemon
CMD [ "nodemon", "index.js" ]