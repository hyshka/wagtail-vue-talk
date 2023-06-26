FROM python:3.8-stretch

RUN apt-get update && \
    apt-get install --no-install-recommends -y nginx  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements ./requirements
RUN pip install --no-cache-dir -r requirements/dev.txt

COPY . /usr/src/app
