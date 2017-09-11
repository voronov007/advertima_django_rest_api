all:
	docker-compose up -d
	docker-compose restart web
	docker-compose ps

django:
	docker-compose restart web
	make log

log:
	docker-compose logs -f web

migrations:
	docker-compose exec web python manage.py makemigrations

migrate:
	docker-compose exec web python manage.py migrate

shell:
	docker-compose exec web python manage.py shell

bash:
	docker-compose exec web bash

chown:
	sudo chown -R ${USER}:${USER} .

dropdb:
	docker-compose stop db
	docker-compose rm -vf db

restartdb:
	docker-compose up -d
	docker-compose restart web
	docker-compose exec web python manage.py migrate
