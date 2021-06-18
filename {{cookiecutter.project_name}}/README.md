<p align="center"><strong>{{ cookiecutter.project_name }}</strong> <em>- {{ cookiecutter.project_short_description }}</em></p>

<p align="center">
<a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions">
    <img src="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
<a href="https://pypi.org/project/{{cookiecutter.project_name}}/">
    <img src="https://badge.fury.io/py/{{cookiecutter.project_name}}.svg" alt="Package version">
</a>
<a href="https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}">
    <img src="https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg" alt="Codecov">
</a>
</p>

---

## Installation

``` bash
pip install {{ cookiecutter.project_name }}
```


## Develop

{% if cookiecutter.tool == 'poetry' -%}
```bash
poetry install
poetry run pre-commit install -t pre-push
```
{%- endif %}
