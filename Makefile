CODE_ROOT := ${PWD}

ifeq ($(SKILL_EXCHANGE_SEARCH)_PORT},)
	export SKILL_EXCHANGE_SEARCH_PORT := 4545
endif

ifeq ($(SKILL_EXCHANGE_SEARCH)_HOST},)
	export SKILL_EXCHANGE_SEARCH_HOST := 0.0.0.0
endif

ifeq (${OS},Windows_NT)
	PYTHON_DIR := .\\venv\\Scripts\\
	PYTHON := .\\venv\\Scripts\\python
	PIP := .\\venv\\Scripts\\pip
	JUPYTER_NOTEBOOK := .\\venv\\Scripts\\jupyter-notebook
	IPYTHON := .\\venv\\Scripts\\ipython
else
	PYTHON_DIR := ./venv/bin/
	PYTHON := ./venv/bin/python
	PIP := ./venv/bin/pip
	JUPYTER_NOTEBOOK := ./venv/bin/jupyter-notebook
	IPYTHON := ./venv/bin/ipython
endif

all: run-dev

clean:
	rm -rf venv && \
	rm -rf *.log*

install-pip:
	${PYTHON} -c "from urllib.request import urlopen; print(urlopen('https://bootstrap.pypa.io/get-pip.py').read().decode('utf-8'))" | ${PYTHON}

venv-setup:
	python3.6 -m venv --without-pip venv
	make install-pip

make-interactive:
	${PIP} install --prefer-binary ipython pylint pep8 flake8 pydocstyle rope jupyter matplotlib isort

venv-dev: venv-setup
	${PIP} install -r requirements/dev.txt --prefer-binary

venv-dev-interactive: venv-dev make-interactive

venv: venv-setup
	${PIP} install -r requirements/prod.txt --prefer-binary

venv-interactive: venv make-interactive

delete-locations-index:
	${PYTHON} -m skill_exchange_search.elastic_search.mapping_creations_deletions.locations.delete_mapping

create-locations-mapping:
	${PYTHON} -m API.location

create-locations-data:
	${PYTHON} -m skill_exchange_search.elastic_search.load_data.location.create_location_data

load-locations-data:
	${PYTHON} -m skill_exchange_search.elastic_search.load_data.location.load_location_data


delete-jobs-index:
	${PYTHON} -m skill_exchange_search.elastic_search.mapping_creations_deletions.jobs.delete_mapping

create-jobs-mapping:
	${PYTHON} -m API.jobs

load-jobs-data:
	${PYTHON} -m skill_exchange_search.elastic_search.load_data.jobs.load_jobs_data

delete-candidates-index:
	${PYTHON} -m skill_exchange_search.elastic_search.mapping_creations_deletions.candidates.delete_mapping

create-candidates-mapping:
	${PYTHON} -m API.candidates

load-candidates-data:
	${PYTHON} -m skill_exchange_search.elastic_search.load_data.candidates.load_candidates_data
