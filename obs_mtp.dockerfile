FROM python:3.6
MAINTAINER AGAMENOR
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapps
WORKDIR /webapps
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
COPY requirements.txt /webapps/
COPY obs_mtp /webapps/
RUN pip install -r /webapps/requirements.txt
# Django service
EXPOSE 8000
   


