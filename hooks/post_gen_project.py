import os
import subprocess


# Add files that should be removed outright under certain conditions here
REMOVE_PATHS = [
    f'{%- if cookiecutter.command_line_interface|lower == "no cli" %}src/{{ cookiecutter.project_name }}/__main__.py{%- endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)


# Set up the project using bash commands here
setup_bash = """
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install .[dev,test]
pre-commit install
pytest tests
"""

subprocess.run(['bash', '-c', setup_bash])
