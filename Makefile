SHELL := /bin/bash -o pipefail
PYTHON ?= python3.9
VENV ?= .venv
ACTIVATE_VENV = source $(VENV)/bin/activate


make_env:
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE_VENV) && \
	$(PYTHON) -m pip install --upgrade pip && \
	pip install -r requirements.txt
	touch $(VENV)

update_env:
	$(ACTIVATE_VENV) && \
	pip install -r requirements.txt
	touch $(VENV)
