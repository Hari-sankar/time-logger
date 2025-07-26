.PHONY: help install run test lint format migrate migration-generate

# Default command
help:
	@echo "Commands:"
	@echo "  install           : Install dependencies"
	@echo "  run               : Run the FastAPI application"
	@echo "  test              : Run tests"
	@echo "  lint              : Lint and format the code"
	@echo "  format            : Format the code with ruff"
	@echo "  migrate           : Apply database migrations"
	@echo "  migration-generate: Generate a new migration"


install:
	uv pip install -e .[dev]

run:
	uv run uvicorn app.main:app --reload

test:
	uv run -- pytest

lint:
	uv run -- ruff check .
	uv run -- ruff format --check .

format:
	uv run -- ruff format .

migrate:
	uv run -- alembic upgrade head

migration-generate:
	uv run -- alembic revision --autogenerate -m "$(m)"
