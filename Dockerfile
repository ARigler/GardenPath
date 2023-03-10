FROM ubuntu

COPY . /app

MAINTAINER ARigler

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip
RUN pip install spacy
RUN python3 -m spacy download en_core_web_sm
CMD python3 /app/gardenpath.py