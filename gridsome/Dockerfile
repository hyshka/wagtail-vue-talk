FROM node:10-alpine
MAINTAINER Oleg Lavrovsky <oleg@utou.ch>

# Set a term for terminal inside the container, can't clear without it
ENV TERM xterm-256color

# Prefix path with global node_modules folder
# This allows npm package binaries to be available everywhere
ENV PATH /app/node_modules/.bin:$PATH

# Update, install packages, and cleanup cache
RUN apk update \
    && apk add git yarn \
    && apk add libwebp libwebp-tools \
    && rm -rf /var/cache/apk/*

# Add the project requirements
# This will add the package.json and yarn.lock if it exists
ADD package*.json /app/
ADD yarn*.lock /app/

# Install the requirements
RUN /bin/sh -c 'cd /app && yarn install --no-optional'

# The code should be symlinked to this directory
WORKDIR /app

# Expose the 8080 port
EXPOSE 8080
