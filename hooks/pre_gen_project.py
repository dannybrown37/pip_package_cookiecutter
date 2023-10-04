import re


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
project_name = '{{ cookiecutter.project_name }}'

if not re.match(MODULE_REGEX, project_name):
    error_message = f'{project_name} is not a valid Python module name!'
    raise ValueError(error_message)
