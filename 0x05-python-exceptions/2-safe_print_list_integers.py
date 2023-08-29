#!/usr/bin/python3
def safe_print_list_integers(len_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(len_list[i]), end="")
            printed += 1
        except (TypeError, ValueError):
            continue
    print("")
    return printed
