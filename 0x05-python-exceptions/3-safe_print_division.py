#!/usr/bin/python3
def safe_print_division(x, y):
    try:
        div = x / y
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
