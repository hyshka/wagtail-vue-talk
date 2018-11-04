.PHONY: build

SHELL := /bin/bash
CONTAINERNAME_BACKEND=wagtail_vue_backend
IMAGENAME_BACKEND=wagtail_vue_backend_image

build: ## Build the backend Docker image
	cp -r website/requirements ./build/backend
	docker build -t $(IMAGENAME_BACKEND) ./build/backend

up: build ## Bring the backend Docker container up
	docker-compose -p wagtail_vue up -d backend || echo 'Already up!'

upwin:  ## Bring the Docker container up for bash on ubuntu folk
	export WINDIR="$(subst /mnt/c,//c,$(CURDIR))/" && make up

lint: build ## Lint the python code.
	docker run -v $(CURDIR):/app $(IMAGENAME_BACKEND) /bin/bash -c 'flake8 website'

down: ## Stop the backend Docker container
	docker-compose -p wagtail_vue stop backend

enter: ## Enter the running backend Docker container
	docker exec -it $(CONTAINERNAME_BACKEND) /bin/bash

clean: ## Stop and remove all Docker containers
	docker-compose -p wagtail_vue down

