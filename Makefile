.PHONY: install format lint test all help

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

format:
	echo "Formatting code..."
	black --line-length=79 .

lint:
	echo "Linting code..."
	flake8 --max-line-length=79 --ignore=E402 .

test:
	pytest tests/

all: install format lint test

help:
	@echo "install - install dependencies"
	@echo "format - format code"
	@echo "lint - lint code"
	@echo "test - run tests"
	@echo "all - install, format, lint, and test"
	@echo "help - print this help message"



