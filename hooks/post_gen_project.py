#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    # Deleting files
    if '{{ cookiecutter.env_workflow }}' == 'pipenv':
        remove_file('requirements.txt')
        remove_file('requirements-dev.txt')
        remove_file('docs/requirements.txt')
    elif '{{ cookiecutter.env_workflow }}' == 'conda':
        remove_file('Pipfile')

    print("Creating first commit (needed for PBR to fully work)")
    # Git add all & commit
    msg_commit = "First commit thx to cookiecutter."

    subprocess.Popen(["git", "init", "."], cwd=PROJECT_DIRECTORY)
    subprocess.Popen(["git", "add", PROJECT_DIRECTORY + "/.*"], cwd=PROJECT_DIRECTORY)
    subprocess.Popen(["git", "commit", "-m", msg_commit], cwd=PROJECT_DIRECTORY)

    if '{{ cookiecutter.env_workflow }}' == 'pipenv':
        print("Setting up a virtual environment")
        subprocess.check_call(["pipenv", "--python", '3.6'])
        subprocess.check_call(["pipenv", "install", "--dev"])

        print("Initial build...")
        venv = subprocess.check_output(
            ["pipenv", "--venv"]).strip().decode('utf8')
        # Cannot use directly `pipenv run`, it requires a TTY, and the
        # --no-interactive options is not available on every version
        subprocess.check_call(
            [os.path.join(venv, "bin", "python"), "setup.py", "sdist"])

        print("Developer environment created. Activate with:")
        print("> pipenv shell")

    print("{} created.".format(PROJECT_DIRECTORY))

    print("You should consider using:")
    if '{{ cookiecutter.env_workflow }}' == 'pipenv':
        print("> pipenv --python 3.6")
        print("> pipenv install --dev")
    else:
        print("> python setup.py develop")
