# TODO project
It's a pet project to practice with layered application architecture.

## Set up
1. Clone project repository;
2. `cd ./todo`
3. `pipenv run install_db_prerequisites`
4. `pipenv install`
5. Up DB: `docker-compose up --build --remove-orphans`

## How to run server:
`uvicorn api.views:app --reload`

## Down DB and clean up
`docker-compose down --volumes --remove-orphans`

TODO: add commands to Makefile
