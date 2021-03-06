import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

project_slug = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_REGEX, project_slug):
    msg = (
        f"ERROR: The project slug '{project_slug}' is not a valid"
        " Python module name. Please do not use a - and use _ instead."
    )
    print(msg)

    # Exit to cancel project
    sys.exit(1)
