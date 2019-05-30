.. |travis| image:: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.svg?branch=master
  :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
.. |codecov| image:: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}
.. |pypi| image:: https://badge.fury.io/py/{{ cookiecutter.project_name }}.svg
  :target: https://pypi.python.org/pypi/{{ cookiecutter.project_name }}/
  :alt: Pypi package
{% if cookiecutter.sphinx_doc == 'yes' %}
.. |readthedocs| image:: https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest
  :target: http://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status
{% endif %}

===============================
{{ cookiecutter.project_name }}
===============================
{% if cookiecutter.sphinx_doc == 'yes' %}
|travis| |codecov| |readthedocs| |pypi|
{% else %}
|travis| |codecov| |pypi|
{% endif %}
{{ cookiecutter.project_short_description }}


Installation
------------

.. code:: bash

    pip install {{ cookiecutter.project_name }}
