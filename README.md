<p align="center"><img width="60%" src="_static/cookiecutter_logo.png" /></p>

--------------------------------------------------------------------------------

## Soft-cookiecutter template

Only a few questions, only a few tools, but everything you need for packaging in python.

See [cookiecutter](https://github.com/audreyr/cookiecutter) for me informations.

- *Standard* or *Pipenv*
- *PBR - Python Build Reasonableness*
- *Travis-CI*: 2 stages: linter + pytest
- *Coverage*: unit test report
- *Sphinx docs*: Documentation ready for generation and publication to *ReadTheDoc*

*Linter*: [pre-commit](https://github.com/pre-commit/pre-commit)
> [flake8](https://github.com/PyCQA/flake8)
> [isort](https://github.com/timothycrosley/isort)
> [yapf](https://github.com/google/yapf)


## Usage

```bash
pip install cookiecutter
cookiecutter https://github.com/gjeusel/soft-cookiecutter
```
