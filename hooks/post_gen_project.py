#!/usr/bin/env python
import shutil
import subprocess
from os import path as osp

PROJECT_DIRECTORY = osp.realpath(osp.curdir)

if __name__ == '__main__':

    if "{{ cookiecutter.sphinx_doc }}" == "no":
        shutil.rmtree(osp.join(PROJECT_DIRECTORY, 'docs'))

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
