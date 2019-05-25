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

- **Standard** or **Pipenv**
- **PBR - Python Build Reasonableness**
- **Sphinx docs**: Documentation ready for generation and publication to **ReadTheDoc**
- **CI** Travis or GitLab:
  - **Linter**: make use of [pre-commit](https://pre-commit.com/)
  - **Pytest**: unit testing (see [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) for distributed testing)
  - **Code Coverage**: testing coverage report using [pytest-cov](https://github.com/pytest-dev/pytest-cov)
  - **PyPI**: deployment only on new tag in master branch

*Linter configuration*:
- [flake8](https://github.com/PyCQA/flake8) for pep8 compliance
- [isort](https://github.com/timothycrosley/isort) for import sorting
- [yapf](https://github.com/google/yapf) for formatting
- [bandit](https://github.com/openstack/bandit) static analyzer on security
  issues
