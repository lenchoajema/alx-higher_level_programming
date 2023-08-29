#!/usr/bin/python3
def safe_print_list(len_list=[], x=0):
    idx = 0
    while idx < x:
        try:
            print("{}".format(len_list[idx]), end="")
        except IndexError:
            break
        idx += 1
    print("")
    return idx
