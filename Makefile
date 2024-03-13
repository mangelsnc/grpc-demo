.PHONY: start-server start-server-daemon stop-server build-server start-python-client build-python-client start-node-client build-node-client
.DEFAULT_GOAL:=help

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Server

start-server:		## 🚀  Start server
	docker compose up grpc_server_python

stop-server: 	## 🙋🏻 Stop server
	docker compose down grpc_server_python

start-server-daemon: 	## 😈  Start detached server
	docker compose up -d grpc_server_python

build-server: 	## 🏗️  Build server
	docker compose build grpc_server_python

##@ Clients

start-python-client: 	## 🚀  Start Python client
	docker compose run grpc_client_python

build-python-client: 	## 🏗️  Build Python client
	docker compose build grpc_client_python

start-node-client: 	## 🚀  Start NodeJS client
	docker compose run grpc_client_nodejs

build-node-client: 	## 🏗️  Build NodeJS client
	docker compose build grpc_client_nodejs
