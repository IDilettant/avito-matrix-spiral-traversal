install:
	poetry install

lint:
	poetry run flake8 mattrav/matrix_traversal.py

isort:
	poetry run isort mattrav tests

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=mattrav --cov-report xml

mypy-check:
	poetry run mypy --namespace-packages tests mattrav

pre-commit:
	poetry run pre-commit run mattrav


.PHONY: test, isort, coverage
