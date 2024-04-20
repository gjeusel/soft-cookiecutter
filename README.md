<p style="flex: 1 1 0%" align="center">
  <img width="45%" src="_static/cookiecutter.svg" />
  <img height="80px" src="_static/cruft.png" />
</p>
<p align="center">
  <em> Everything you need for a modern python project/package. </em>
</p>

---

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

#### CI Github actions

- **Linter & Formatter**: [ruff](https://github.com/charliermarsh/ruff)
- **Type Checker**: [mypy](https://github.com/python/mypy)
- **Pytest**: unit testing
- **Code Coverage**: [coverage](https://github.com/nedbat/coveragepy) & [smokeshow](https://github.com/samuelcolvin/smokeshow)
- **PyPI**: deployment only on new tag in main branch
