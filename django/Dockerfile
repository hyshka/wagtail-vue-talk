FROM python:3.6-stretch

RUN apt-get update && \
    apt-get install --no-install-recommends -y nginx  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY website/requirements ./requirements
RUN pip install --no-cache-dir -r requirements/dev.txt

COPY . /usr/src/app

# Set the needed variables
#ENV PYTHONPATH=/app/website/wagtail_vue:/app/website/wagtail_vue/apps
