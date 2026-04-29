.PHONY: rebuild
rebuild: down-all create-model build

down-all:
	docker-compose down --remove-orphans
create-model:
	python -m brain.create_model
build:
  docker-compose build --no-cache

