FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install -y gettext

RUN useradd -u 1000 linux-user

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

WORKDIR /app/site

