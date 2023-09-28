{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{% endif %}


{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
@click.option('--arg', '-a' help='', type=str)
def main(arg):
    ""f"Console script for {{cookiecutter.project_name}}."""
    return arg
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    ""f"Console script for {{cookiecutter.project_name}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg', '-a', nargs='*')
    args = parser.parse_args()
    return args.arg
{%- endif %}
