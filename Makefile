.PHONY: build

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-30s\\033[0m %s\\n", $$1, $$2}'

build: ## Build the Docker image
	docker-compose -p wagtail_vue build

up: build ## Bring the container up
	docker-compose -p wagtail_vue up -d

down: ## Stop the container
	docker-compose -p wagtail_vue stop

enter: ## Enter the running container
	docker-compose -p wagtail_vue exec backend /bin/bash

enter_frontend: ## Enter the running container
	docker-compose -p wagtail_vue exec frontend /bin/bash

clean: down ## Remove stoped containers
	docker-compose -p wagtail_vue rm

lint: ## Run linters on code
	docker-compose -p wagtail_vue exec backend bash -c "flake8 ."
	docker-compose -p wagtail_vue exec backend bash -c "black --diff --check --exclude 'migrations|node_modules' ."

lint_frontend: ## Run linters on code
	docker-compose -p wagtail_vue exec frontend bash -c "npm run --silent lint"
