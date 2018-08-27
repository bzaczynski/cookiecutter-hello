#!/usr/bin/env python

"""
Usage:
$ python {{ cookiecutter.project_name }}_script.py
"""

import sys

from {{ cookiecutter.project_name }}.world import say_hello


def main():
    """Application entry point."""
    say_hello()


if __name__ == '__main__':
    sys.exit(main())
