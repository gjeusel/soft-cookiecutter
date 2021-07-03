<p align="center"><img width="60%" src="_static/cookiecutter_logo.png" /></p>

--------------------------------------------------------------------------------

## Soft-cookiecutter template

Everything you need for packaging in python. See [cookiecutter](https://github.com/audreyr/cookiecutter) for me informations.

## Usage

```bash
pip install cookiecutter
cookiecutter https://github.com/gjeusel/soft-cookiecutter
```

## Details

- Tooling choice:
  - **PBR** - Python Build Reasonableness (conda / pip)
  - **poetry** - [poetry-version-plugin](https://github.com/tiangolo/poetry-version-plugin)

- **mkdocs**: generate beautiful documentation easily with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

- **CI** Github actions:
  - **Linter**: make use of [pre-commit](https://pre-commit.com/) with "local repos" (keep pinned linting reqs in sync)
  - **Pytest**: unit testing (see [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) for distributed testing)
  - **Code Coverage**: testing coverage report using [pytest-cov](https://github.com/pytest-dev/pytest-cov)
  - **PyPI**: deployment only on new tag in master branch


*Linter + Formatter configuration*:
- [flake8](https://github.com/PyCQA/flake8) for pep8 compliance (extra: [flake8-builtins](https://github.com/gforcada/flake8-builtins) + [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear))
- [mypy](https://github.com/python/mypy) for static type checking (strict by default)
- [isort](https://github.com/timothycrosley/isort) for import sorting (with black profile)
- [black](https://github.com/psf/black) for formatting
- [bandit](https://github.com/openstack/bandit) static analyzer on security
  issues


## Remarks

- The Github workflow "test-suite" needs a secrets named `CODECOV_TOKEN` to publish to codecov
- The Github workflow "publish" needs a secrets named `PYPI_TOKEN` to publish to public pypi
- The Github workflow "publish" is triggered on new git tag
