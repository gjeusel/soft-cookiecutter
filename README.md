<p align="center">
  <h1> Soft </h1>
  <img width="60%" src="_static/cookiecutter_logo.png" />
  <br/>
  <em> Everything you need for a modern python project/package. </em>
</p>

---

## Soft-cookiecutter template

See [cookiecutter](https://github.com/audreyr/cookiecutter) and [cruft](https://github.com/cruft/cruft) for more informations.

## Usage

```bash
pip install -y cookiecutter cruft
```

```bash
cruft create https://github.com/gjeusel/soft-cookiecutter
```

## Details

#### Tooling choices

- **PEP 621**: pyproject.toml (everything)
- **Hatchling**: dynamic versioning (based on git)
- **pre-commit**: a framework for managing and maintaining multi-language pre-commit hooks
- **mkdocs**: generate beautiful documentation easily with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

#### CI Github actions:

- **Linter & Formatter**: [ruff](https://github.com/charliermarsh/ruff) + [black](https://github.com/psf/black)
- **Type Checker**: [mypy](https://github.com/python/mypy)
- **Pytest**: unit testing
- **Code Coverage**: testing coverage report using [pytest-cov](https://github.com/pytest-dev/pytest-cov)
- **PyPI**: deployment only on new tag in master branch

#### Remarks

- The Github workflow "test-suite" needs a secrets named `CODECOV_TOKEN` to publish to codecov
- The Github workflow "publish" needs a secrets named `PYPI_TOKEN` to publish to public pypi
- The Github workflow "publish" is triggered on new git tag
