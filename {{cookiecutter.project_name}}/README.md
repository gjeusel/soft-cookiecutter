# {{ cookiecutter.project_name }}

[![Build Status](https://travis-ci.com/{{ cookiecutter.github_username  }}/{{ cookiecutter.project_name  }}.svg?branch=master)(https://travis-ci.com/{{ cookiecutter.github_username  }}/{{ cookiecutter.project_name  }})
[![Codecov]](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg)(https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}})
[![PyPI]](https://badge.fury.io/py/{{ cookiecutter.project_name  }}.svg)(https://pypi.python.org/pypi/{{ cookiecutter.project_name  }}/)

{% if cookiecutter.sphinx_doc == 'yes' %}
[![readthedocs]](https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest)(http://{{ cookiecutter.project_name  }}.readthedocs.io/en/latest/?badge=latest)
{% endif %}

{{ cookiecutter.project_short_description }}


## Installation

``` bash
    pip install {{ cookiecutter.project_name }}
```
