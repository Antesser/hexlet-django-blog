start:
	poetry run python3 manage.py runserver 4000
install:
	poetry install
migrate:
	poetry run python manage.py migrate
check:
	poetry check	