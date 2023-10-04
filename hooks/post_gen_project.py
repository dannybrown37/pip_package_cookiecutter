import os
import sys


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
