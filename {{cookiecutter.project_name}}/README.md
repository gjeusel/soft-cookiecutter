<p align="center">
  <h1> {{ cookiecutter.project_name }} </h1>
  <p>
    <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions">
        <img src="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/workflows/Test%20Suite/badge.svg" alt="Test Suite" onerror="this.style.display='none'">
    </a>
    <a href="https://pypi.org/project/{{cookiecutter.project_name}}/">
        <img src="https://badge.fury.io/py/{{cookiecutter.project_name}}.svg" alt="Package version" onerror="this.style.display='none'">
    </a>
    <a href="https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}">
        <img src="https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg" alt="Codecov" onerror="this.style.display='none'">
    </a>
    <!-- <a href="github page link for mkdocs"> -->
    <!--   <img src="https://img.shields.io/badge/mkdocs-pages-brightgreen" alt="MKDocs github page"> -->
    <!-- </a> -->
    <a href="https://github.com/pre-commit/pre-commit">
        <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit">
    </a>
  </p>
  <br/>
  <em>{{ cookiecutter.project_short_description }}</em>

<p align="center">
</p>

---

## Installation

```bash
pip install {{ cookiecutter.project_name }}
```

### Developper

##### Install

```bash
make install
```

##### Launch tests:

```bash
pytest
```

##### Write docs:

```bash
mkdocs serve --watch .
```

### Update Cookiecutter Template

```bash
cruft update --skip-apply-ask --allow-untracked-files --project-dir .
```
