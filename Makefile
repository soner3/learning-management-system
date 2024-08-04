up:
	docker-compose up -d

down:
	docker-compose down

down-v:
	docker-compose down -v

build:
	docker-compose up --build

makemigrations:
	docker-compose run --rm django python manage.py makemigrations

migrate:
	docker-compose run --rm django python manage.py migrate

collectstatic:
	docker-compose run --rm django python manage.py collectstatic

superuser:
	docker-compose run --rm django python manage.py createsuperuser

logs:
	docker-compose logs

logs-django:
	docker-compose django logs
