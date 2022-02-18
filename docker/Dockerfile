FROM --platform=linux/amd64 python:3.10.1

MAINTAINER Anish dhanka anish@bjshomedelivery.com

RUN apt update; apt install -y gunicorn

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app

WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 5000

ENTRYPOINT ["gunicorn","app:app","-b","0.0.0.0:5000"]