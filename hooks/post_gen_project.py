#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    print("Creating first commit (needed for PBR to fully work)")
    # Git add all & commit
    msg_commit = "First commit thx to cookiecutter."

    subprocess.call(["git", "init", "."], cwd=PROJECT_DIRECTORY)
    subprocess.call(["git", "add", "."], cwd=PROJECT_DIRECTORY)
    subprocess.call(["git", "commit", "-m", msg_commit], cwd=PROJECT_DIRECTORY)

    print("{} created.".format(PROJECT_DIRECTORY))

    msg = ("You should consider using:",
           "pip install --editable {{ cookiecutter.project_name }}.")
    print("\n".join(msg))
