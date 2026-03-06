default: install lint test

install:
    uv sync

test *args:
    uv run pytest {{args}}

lint:
    uv run ruff format
    uv run ruff check
    uv run auto-typing-final .
    uv run flake8 .
    uv run mypy .

lint-ci:
    uv run ruff format
    uv run ruff check
    uv run auto-typing-final .
    uv run flake8 .
    uv run mypy .

publish:
    rm -rf dist
    uv version $GITHUB_REF_NAME
    uv build
    uv publish --token $PYPI_TOKEN
