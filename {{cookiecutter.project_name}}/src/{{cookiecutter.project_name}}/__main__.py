"""Entry point for CLI to handle args"""

{% if cookiecutter.command_line_interface|lower == 'click' %}
import click

{% elif cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse

{% endif %}

{%- if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
@click.option('--arg', '-a', help='', type=str)
def main(arg):
    """Console script for {{cookiecutter.project_name}}."""
    return arg
{%- elif cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_name}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg', '-a', nargs='*')
    args = parser.parse_args()
    return args.arg
{%- endif %}
