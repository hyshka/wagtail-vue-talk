# build command is fake
.PHONY: build

# variables
CONTAINERNAME=vue_talk
IMAGENAME=vue_talk

# list available commands with description
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## build image
	docker build -t $(IMAGENAME) .

up: build ## build image and start container
	docker run -d -p 8080 -v $(CURDIR):/app -v /app/node_modules --name $(CONTAINERNAME) $(IMAGENAME) /bin/sh -c 'while true; do echo hi; sleep 1; done;' || echo 'Already up!'

enter: ## enter container
	docker exec -it $(CONTAINERNAME) /bin/sh

stop: ## stop container
	docker stop $(CONTAINERNAME) || echo 'No container to stop'

clean: stop ## stop and remove container
	docker rm $(CONTAINERNAME) || echo 'No container to remove'
