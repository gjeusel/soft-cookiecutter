{% if cookiecutter.tool == 'pbr' -%}
from pkg_resources import get_distribution

try:
    __version__ = get_distribution('{{ cookiecutter.project_slug }}').version
except Exception:
    __version__ = 'Version not found.'
{% else -%}
import dunamai as _dunamai

__version__ = _dunamai.get_version(
    __name__, first_choice=_dunamai.Version.from_any_vcs
).serialize(style=_dunamai.Style.Pep440, bump=True)
{%- endif %}
