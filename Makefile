install:
	python -m pip install --upgrade pip
	pip install poetry
	poetry install

lint:
	poetry run ruff .

format:
	poetry run black .

test:
	poetry run pytest

clean:
	git clean -Xdf
