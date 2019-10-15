FROM python:3.6-slim-stretch

LABEL maintainer="Travis Howard <travis.howard.tj@gmail.com>"

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

ENV DJANGO_SETTINGS_MODULE=Kost.settings

RUN apt update && apt -y upgrade && pip install --trusted-host pypi.python.org -r requirements.txt && \
  python manage.py makemigrations && python manage.py migrate

EXPOSE 9898

CMD ["gunicorn", "Kost.wsgi:application", "--bind", "0:9898"]
