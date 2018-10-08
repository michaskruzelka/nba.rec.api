FROM python:3.7.0-alpine
MAINTAINER Michael Marchanka <michaskruzelka@protonmail.ch>



COPY . /app
WORKDIR /app

RUN pip install pipenv

ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

ONBUILD RUN pipenv install --deploy --system

EXPOSE 5000
#CMD ["python", "app.py"]
#CMD gunicorn --bind 0.0.0.0:$PORT wsgi