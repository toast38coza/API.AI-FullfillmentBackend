FROM python:3.4
ENV PYTHONUNBUFFERED 1
ENV WITH_DOCKER True
RUN mkdir -p /bot
WORKDIR /bot
ADD requirements.txt requirements-dev.txt /bot/
RUN pip install -U pip
RUN pip install -r requirements.txt -r requirements-dev.txt
ADD . /bot/
