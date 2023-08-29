import ctypes

def print_python_list(p):
    size = ctypes.c_ssize_t.from_address(id(p) + ctypes.sizeof(ctypes.c_ssize_t) * 2).value
    alloc = ctypes.c_ssize_t.from_address(id(p) + ctypes.sizeof(ctypes.c_ssize_t) * 3).value
    type_name = p.__class__.__name__

    print("[*] Python list info")
    if type_name != 'list':
        print("  [ERROR] Invalid List Object")
        return

    print("[*] Size of the Python List =", size)
    print("[*] Allocated =", alloc)

    for i, item in enumerate(p):
        type_name = item.__class__.__name__
        print("Element {}: {}".format(i, type_name))
        if type_name == "bytes":
            print_python_bytes(item)
        elif type_name == "float":
            print_python_float(item)

def print_python_bytes(p):
    size = ctypes.c_ssize_t.from_address(id(p) + ctypes.sizeof(ctypes.c_ssize_t) * 2).value
    bytes_data = (ctypes.c_char * size).from_address(id(p) + ctypes.sizeof(ctypes.c_ssize_t) * 3)

    print("[.] bytes object info")
    if p.__class__.__name__ != 'bytes':
        print("  [ERROR] Invalid Bytes Object")
        return

    print("  size:", size)
    print("  trying string:", bytes_data.raw.decode('utf-8', 'replace'))

    if size >= 10:
        size = 10

    print("  first {} bytes: ".format(size), end="")
    for i in range(size):
        print("{:02x}".format(ord(bytes_data[i])), end=" ")
    print()

def print_python_float(p):
    float_val = ctypes.c_double.from_address(id(p) + ctypes.sizeof(ctypes.c_double)).value

    print("[.] float object info")
    if p.__class__.__name__ != 'float':
        print("  [ERROR] Invalid Float Object")
        return

    print("  value:", float_val)

# Test with an example list
example_list = [b'hello', 3.14, b'world', 2.718]
print_python_list(example_list)
