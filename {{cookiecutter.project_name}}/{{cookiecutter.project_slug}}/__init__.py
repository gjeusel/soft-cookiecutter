{% if cookiecutter.tool == 'pbr' -%}
from pkg_resources import get_distribution

try:
    __version__ = get_distribution('{{ cookiecutter.project_slug }}').version
except Exception:
    __version__ = 'Version not found.'
{% endif %}
