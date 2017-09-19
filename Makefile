start:
	docker-compose up -d
	docker-compose restart advertima_web
	docker-compose ps

stop:
	docker-compose stop

init:
	docker-compose build
	docker-compose up -d
	docker-compose restart advertima_web
	docker-compose ps
	sleep 3
	docker-compose exec dashboard_db bash -c "psql -d advertima_db -U advertima_admin -f /dumps/dump.sql"
	docker-compose exec advertima_web python manage.py migrate

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

dump:
	docker-compose exec dashboard_db bash -c "pg_dump -U advertima_admin -d advertima_db > /dumps/dump.sql"

