#!/usr/bin/env python
import shutil
import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path(".").absolute()


def remove(filepath):
    target = PROJECT_DIRECTORY / filepath

    if not target.exists():
        return

    if target.is_dir():
        shutil.rmtree(target, ignore_errors=True)
    else:
        target.unlink()


def main():
    # Docker cleaning
    if "{{ cookiecutter.dockerfile }}" != "yes":
        remove("Dockerfile")
        remove("requirements")

    # Remove licenses templates
    remove("licenses")

    # Guard in case of template refresh using [cruft](https://github.com/cruft/cruft)
    # TODO: use tempfile.gettempdir() to deduce on any platform
    is_cruft_update = PROJECT_DIRECTORY.as_posix().startswith("/private")
    if is_cruft_update:
        return

    # git init
    subprocess.check_call(["git", "init", "."], cwd=PROJECT_DIRECTORY)

    # print notes on easy configs steps

    notes = [
        "- To create the github repository:",
        "  > gh repo create --public --description '{{ cookiecutter.project_short_description }}'",
        "",
        "- To commit and push generated template:",
        "  > {}".format(
            " && ".join(
                [
                    "git add .",
                    "git commit -m 'add(first-commit): templated by soft-cookiecutter'",
                    "git push --set-upstream origin main",
                ]
            )
        ),
        "",
        "- To configure the gh repo:",
        "  * set up github pages for mkdocs, create a branch called `gh-pages`",
        "    > git checkout -b gh-pages && git push origin gh-pages && git checkout main",
        "    and configure github pages for this repo at:",
        "    https://github.com/{{ cookiecutter.github_username }}/{ cookiecutter.project_name }}/settings/pages",
        "",
        "  * set up the action to publish to pypi in CI:",
        "    > gh secret set PYPI_TOKEN",
        "",
        "  * set up the action to publish coverage html to smokeshow:",
        "    > pip install smokeshow && smokeshow generate-key",
        "    > gh secret set SMOKESHOW_AUTH_KEY",
        "",
        "- To create your conda env:",
        "  > conda create --name {{ cookiecutter.project_name}} python=3.10 --yes",
    ]

    print("\n".join(notes))


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as err:
        print(f"Failed to run '{err.cmd}' commands. ({err})")
    except OSError:
        print("Missing 'git' in PATH.")

    print(f"{PROJECT_DIRECTORY.as_posix()} created.")
