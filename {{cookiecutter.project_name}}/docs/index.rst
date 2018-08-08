:github_url: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}

Welcome to {{ cookiecutter.project_name }}'s documentation!
==================================================

{{ cookiecutter.project_short_description }}

.. toctree::
   :maxdepth: 2
   :caption: Notes

   quickstart <notes/quickstart>


.. toctree::
   :maxdepth: 2
   :caption: Package Reference

   {{ cookiecutter.project_slug }}.cli <src/cli>


.. toctree::
   :maxdepth: 1
   :caption: Miscellaneous

   authors
   changelog

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
