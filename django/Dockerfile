FROM ubuntu:16.04
MAINTAINER Kalob Taulien <kalob@kalob.io>

# Needed for better experience in container terminal
ENV TERM=xterm-256color

# Update and install
RUN apt-get update && apt-get install -y \
      git \
      wget \
      # Python, remove 3 for wagtail sites
      python3-dev \
      python3-pip

# Set the encoding to avoid issues with internationalization packages.
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN pip3 install --upgrade pip

# Add the project requirements
ADD website/requirements /opt/requirements

# Install the requirements, remove 3 for wagtail
RUN /bin/bash -c 'cd /opt \
      && pip3 install -r requirements/dev.txt'

# Set the needed variables
ENV PYTHONPATH=/app/website/wagtail_vue:/app/website/wagtail_vue/apps
ENV DJANGO_SETTINGS_MODULE=wagtail_vue.settings.dev

# change to /app for the working directory, you should mount the local dir volume here
WORKDIR /app

EXPOSE 8000

# Add bash aliases
ADD bash_aliases /root/.bash_aliases
