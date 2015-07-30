#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'operation.env')
    execute_from_command_line(sys.argv)

