############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu/Debia
############################################################


# Set the base image to Ubuntu
FROM python:3.10

MAINTAINER Stefan Hesse


ADD requirements.txt /requirements.txt
ADD python/ingest_data.py /ingest_data.py
ADD python/query.py /query.py
ADD python/client.py /client.py
ADD container-run.sh /run.sh
ADD data/data.json /data.json
ADD data/schema.json /schema.json
ADD data/search.json /search.json

RUN pip install -r /requirements.txt

RUN bash

ENTRYPOINT ["sh","/run.sh"]
