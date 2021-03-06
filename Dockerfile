FROM python:3.7-slim

LABEL maintainer="Travis Howard <travis.howard.tj@gmail.com>"

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY . /usr/src/app/