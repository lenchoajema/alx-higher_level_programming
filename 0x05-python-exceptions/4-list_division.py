#!/usr/bin/python3
def list_division(len_list_1, len_list_2, list_length):
    newList = []
    for i in range(list_length):
        div = 0
        try:
            div = len_list_1[i] / len_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            newList.append(div)
    return newList
