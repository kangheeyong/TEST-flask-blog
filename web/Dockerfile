FROM python:3.8

RUN apt-get update
RUN apt-get install redis-tools -y

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask-wtf
RUN pip install flask-sqlalchemy
RUN pip install flask-bcrypt
RUN pip install flask-login
RUN pip install flask-mail
RUN pip install email_validator
RUN pip install pytest
RUN pip install Pillow
RUN pip install gunicorn

RUN mkdir -p /app

WORKDIR /app
