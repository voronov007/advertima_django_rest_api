all:
	docker-compose up -d
	docker-compose restart advertima_web
	docker-compose ps

django:
	docker-compose restart advertima_web
	make log

log:
	docker-compose logs -f advertima_web

migrations:
	docker-compose exec advertima_web python manage.py makemigrations

migrate:
	docker-compose exec advertima_web python manage.py migrate

shell:
	docker-compose exec advertima_web python manage.py shell

bash:
	docker-compose exec advertima_web bash

chown:
	sudo chown -R ${USER}:${USER} .

dropdb:
	docker-compose stop dashboard_db
	docker-compose rm -vf dashboard_db

restartdb:
	docker-compose up -d
	docker-compose restart advertima_web
	docker-compose exec advertima_web python manage.py migrate
