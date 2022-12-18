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

    # git remote add origin
    ssh_url = "git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git"
    subprocess.check_call(
        ["git", "remote", "add", "origin", ssh_url],
        cwd=PROJECT_DIRECTORY,
    )

    https_url = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git"
    notes = [
        "- To create the github repository:",
        "  > gh repo create --public --description '{{ cookiecutter.project_short_description }}'"
        f" --template 'https://github.com/gjeusel/soft-cookiecutter' {https_url}",
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
