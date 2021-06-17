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
        ]
        for f in to_remove:
            remove(f)
    else:  # pbr
        remove("pyproject.toml")

    remove("licenses")

    # git init
    subprocess.call(["git", "init", "."], cwd=PROJECT_DIRECTORY)

    print("{} created.".format(PROJECT_DIRECTORY.as_posix()))
