.PHONY: install
install:
	python -m pip install --upgrade pip
	pip install poetry
	poetry install

.PHONY: lint
lint:
	poetry run ruff .

.PHONY: format
format:
	poetry run black .

.PHONY: test
test:
	poetry run pytest

.PHONY: clean
clean:
	git clean -Xdf
