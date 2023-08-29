#!/usr/bin/python3
def magic_calculation(len_a, len_b):
    result = 0
    for i in range(1, 3):
        try:
            if i > len_a:
                raise Exception("Too far")
            else:
                result += (len_a**len_b)/i
        except:
            result = len_b + len_a
            break
    return result

#import dis
#dis.dis(magic_calculation)
