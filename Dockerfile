FROM python:3.8
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt
COPY . /usr/src/app
#ENTRYPOINT ["./docker-entrypoint.sh"]

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]