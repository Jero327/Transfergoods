FROM python:3.8
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt
COPY . /usr/src/app
EXPOSE 8000
CMD exec gunicorn django_auth_example.wsgi:application --bind 0.0.0.0:8000