build:
	docker compose build

down:
	docker compose down

runserver:
	docker compose up

makemigrations:
	docker compose run --rm app alembic revision --autogenerate -m "$(MSG)"

migrate:
	docker compose run --rm app alembic upgrade head

test:
	docker compose run --rm app python -m unittest discover -v -s app/tests/$(DIR)