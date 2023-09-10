.PHONY : install_dependencies
install_dependencies:
	pipenv sync

.PHONY : tests
tests:
	pipenv run pytest tests/

.PHONY : clean
clean:
	rm -rf .venv/ .pytest_cache/

.PHONY : run
run:
	pipenv run python tli/tli.py

.PHONY : lint
lint:
	pipenv run black .

.PHONY : check_types
check_types:
	pipenv run mypy .