#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(len_value):
    try:
        print("{:d}".format(len_value))
        return (True)
    except (TypeError, ValueError) as e:
        stderr.write("Exception: {}\n".format(e))
        return (False)
