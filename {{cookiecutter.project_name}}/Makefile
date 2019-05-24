.PHONY: build

MODULE:={{ cookiecutter.project_slug }}

{% if cookiecutter.env_workflow == 'pipenv' %}
all: dev style checks requirements.txt build dists doc test-unit test-coverage

dev:
	pipenv install --dev --python 3.6

install-local:
	pipenv install --python 3.6

install-system:
	pipenv install --system

style: isort black

isort:
	pipenv run isort -y

#black:
#  pipenv run black $(MODULE)

yapf:
	pipenv run yapf $(MODULE)

checks:
	pipenv check

flake8:
	pipenv run python setup.py flake8

test-unit:
	pipenv run pytest --cov $(MODULE) --cov-report term-missing

test-coverage:
	pipenv run py.test  --cov $(MODULE) --cov-report term-missing --cov-report html

# generate requirements.txt frm Pipfile.lock
# needed until PBR supports `Pipfile`
requirements.txt:
	pipenv run pipenv_to_requirements -f

Pipfile.lock:    Pipfile
	pipenv lock

dists: requirements.txt sdist wheels

sdist:
	pipenv run python setup.py sdist

wheels:
	pipenv run python setup.py bdist_wheel

doc:
	pipenv run python setup.py build_sphinx

publish:
	pipenv run twine upload --repository-url https://upload.pypi.org/legacy/ dist/
{% elif cookiecutter.env_workflow == 'conda' %}
all: dev style sdists doc test-unit test-coverage

dev: python setup.py develop

style: isort yapf

isort:
	isort -y

#black:
#  black $(MODULE)

yapf:
	yapf $(MODULE)

flake8:
	python setup.py flake8

test-unit:
	py.test --cov $(MODULE) --cov-report term-missing

test-coverage:
	py.test  --cov $(MODULE) --cov-report term-missing --cov-report html

dists: sdist wheels

sdist:
	python setup.py sdist

wheels:
	python setup.py bdist_wheel

doc:
	python setup.py build_sphinx

publish:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/
{% endif %}

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -rf .pytest_cache/

# aliases to gracefully handle typos on poor dev's terminal
check: checks
devel: dev
develop: dev
dist: dists
install: install-system
pypi: publish
styles: style
test: test-unit
unittest: test-unit
wheel: wheels
