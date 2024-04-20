<h1> {{ cookiecutter.project_name }} </h1>

<p align="center">
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions?query=workflow%3ACI+branch%3Amain">
      <img src="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/workflows//CI/badge.svg?event=push&branch=main" alt="Test Suite" onerror="this.style.display='none'">
  </a>
  <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}" alt="Test Coverage" onerror="this.style.display='none'">
      <img src="https://coverage-badge.samuelcolvin.workers.dev/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/{{cookiecutter.project_name}}/">
      <img src="https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}" alt="Package version" onerror="this.style.display='none'">
  </a>
  <a href="https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_name}}/">
    <img src="https://img.shields.io/badge/mkdocs-pages-brightgreen" alt="MKDocs github page">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
      <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit">
  </a>
</p>

<p align="center">
  <em>{{ cookiecutter.project_short_description }}</em>
</p>

---

## Installation

```bash
pip install {{ cookiecutter.project_name }}
```
