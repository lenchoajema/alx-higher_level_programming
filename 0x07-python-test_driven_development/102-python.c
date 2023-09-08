#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints Python strings
 * @p: PyObject pointer
 */
void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        Py_UNICODE *str = PyUnicode_AsUnicode(p);
        Py_ssize_t len = PyUnicode_GetLength(p);

        printf("[.] string object info\n");
        printf("  type: %s\n", Py_TYPE(p)->tp_name);
        printf("  length: %ld\n", len);
        printf("  value: %ls\n", str);
    }
    else
    {
        fprintf(stderr, "[!] Invalid String Object\n");
    }
}
