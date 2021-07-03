#!/usr/bin/env python
import shutil
import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path(".").absolute()


def remove(filepath):
    target = PROJECT_DIRECTORY / filepath

    if target.is_dir():
        shutil.rmtree(target, ignore_errors=True)
    else:
        target.unlink()


if __name__ == "__main__":

    if "{{ cookiecutter.mkdocs }}" == "yes":
        remove("docs")
        remove("mkdocs.yml")

    if "{{ cookiecutter.tool }}".lower() == "poetry":
        to_remove = [
            "requirements.txt",
            "requirements-dev.txt",
            "setup.cfg",
            "setup.py",
            ".coveragerc",
            ".flake8",
        ]
        for f in to_remove:
            remove(f)
    else:  # pbr
        remove("pyproject.toml")

    if "{{ cookiecutter.dockerfile }}" != "yes":
        remove("Dockerfile")

    remove("dockerfiles")
    remove("licenses")

    # git init
    subprocess.call(["git", "init", "."], cwd=PROJECT_DIRECTORY)

    print(f"{PROJECT_DIRECTORY.as_posix()} created.")

    if "{{ cookiecutter.tool }}".lower() == "poetry":
        print("Notes:")
        print("    - Make sure you got poetry ^1.2")
        print("      > poetry --version")
        print("    - Don't forget to install poetry version plugin")
        print("      > poetry plugin add poetry-version-plugin")
        print("    - Then install")
        print("      > poetry install")
