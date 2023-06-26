FROM node:12-alpine

# Prefix path with global node_modules folder
# This allows npm package binaries to be available everywhere
ENV PATH /app/node_modules/.bin:$PATH

RUN apk update \
     && apk add bash \
     && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

COPY package*.json ./

RUN /bin/sh -c 'cd /app && npm install && npm cache clean --force'

COPY . /usr/src/app
