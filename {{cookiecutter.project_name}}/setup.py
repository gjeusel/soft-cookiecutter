from setuptools import setup

{% if cookiecutter.sphinx_doc == 'yes' %}
try:
    from sphinx.setup_command import BuildDoc
except ImportError:
    BuildDoc = None

setup(
    setup_requires=['pbr'],
    pbr=True,
    cmdclass={'build_sphinx': BuildDoc},
)
{% else %}
setup(setup_requires=['pbr'], pbr=True)
{% endif %}
