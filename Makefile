install_dependencies:
	pipenv sync

.PHONY : tests
tests:
	pipenv run pytest tests/

clean:
	rm -rf .venv/ .pytest_cache/

run:
	pipenv run python tli/tli.py