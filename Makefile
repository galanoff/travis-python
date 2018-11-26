PYTHONPATH?=src

.PHONY: setup
setup:
		echo VER=${VER}
		python --version
		pip install flake8

.PHONY: lint
lint:
		flake8

.PHONY: tests
tests:
		env PYTHONPATH=$(PYTHONPATH) python -m unittest discover -s tests