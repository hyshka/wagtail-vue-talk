FROM node:10-alpine
MAINTAINER Bryan Hyshka <bryan@hyshka.com>

# Set a term for terminal inside the container, can't clear without it
ENV TERM xterm-256color

# Prefix path with global node_modules folder
# This allows npm package binaries to be available everywhere
ENV PATH /app/node_modules/.bin:$PATH

# Update, install, and cleanup
# RUN apk update \
    # && apk add git \
    # && rm -rf /var/cache/apk/*

# Add the project requirements
# This will add the package.json and package-lock.json if it exists
ADD package*.json /app/

# Install the requirements
RUN /bin/sh -c 'cd /app && npm install && npm cache clean --force'

# The code should be symlinked to this directory
WORKDIR /app

# Expose the 8080 port
EXPOSE 8080
