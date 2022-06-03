.ONESHELL:

.PHONY: default up_db wait_for_db run_locally run clean

default: up_db wait_for_db run

up_db:
	@docker-compose up --build --remove-orphans -d database

wait_for_db:
	@until docker container exec -it database pg_isready;
	do
		>&2 echo "waiting for Postgres... 😴";
		sleep 5;
	done
	@echo "database has started"

run:
	@docker-compose up --build --remove-orphans -d adminer
	@docker-compose up --build --remove-orphans todo

run_locally:
	@uvicorn api.views:app --reload

clean:
	@docker-compose down --volumes --remove-orphans
