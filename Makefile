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

clean:
	rm -rf venv && \
	rm -rf *.log*

install-pip:
	${PYTHON} -c "from urllib.request import urlopen; print(urlopen('https://bootstrap.pypa.io/get-pip.py').read().decode('utf-8'))" | ${PYTHON}

venv-setup:
	python3 -m venv --without-pip venv
	make install-pip

venv: venv-setup
	${PIP} install -r requirements.txt --prefer-binary

delete-locations-index:
	${PYTHON} -m API.location.delete_index

create-locations-mapping:
	${PYTHON} -m API.location.create_index

load-locations-data:
	${PYTHON} -m API.location

delete-jobs-index:
	${PYTHON} -m API.job.delete_index

create-jobs-mapping:
	${PYTHON} -m API.jobs.create_index

load-jobs-data:
	${PYTHON} -m API.jobs

delete-candidates-index:
	${PYTHON} -m API.candidate.delete_index

create-candidates-mapping:
	${PYTHON} -m API.candidate.create_index

load-candidates-data:
	${PYTHON} -m API.candidate
