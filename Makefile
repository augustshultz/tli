.PHONY : install_dependencies
install_dependencies:
	uv sync

.PHONY : tests
tests:
	uv run pytest tests/

.PHONY : clean
clean:
	rm -rf .venv/ .pytest_cache/

.PHONY : run
run:
	uv run python -m tli.tli

.PHONY : format
format:
	uv run ruff format .

.PHONY : check_types
check_types:
	uv run mypy .

.PHONY : lint
lint:
	uv run ruff check .