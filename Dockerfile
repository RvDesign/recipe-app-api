FROM python:3.9-alpine
MAINTAINER RvDesign App Developer

ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -D running applications only
RUN adduser -D user
USER user
