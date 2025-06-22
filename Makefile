# Run main script.
.PHONY: run
run:
	python3 src/main.py

# Clean up environment.
.PHONY: clean
clean:
	@read -p "Make sure you have exited the virtual environment before running 'make clean'. Proceed? (y/n): " confirm && [ "$$confirm" = "y" ]
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -rf __pycache__/ *.pyc *.pyo .pytest_cache .ruff_cache .venv

# Format files, need to be run in the virtual environment.
.PHONY: format
format:
	ruff format src tests

# Run tests, need to be run in the virtual environment.
.PHONY: test
test:
	python3 -m pytest -s -v