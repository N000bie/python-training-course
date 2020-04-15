# -*- encoding: utf-8 -*-
import ctypes
import ctypes.util
import sys

if 'win' in sys.platform:
    libc = ctypes.cdll.msvcrt
else:
    libc_pos = ctypes.util.find_library('c')
    if libc_pos is None:
        raise RuntimeError(
            'cannot locate libc, are you running in Linux '
            + 'and/or have libc installed?'
        )
    libc = ctypes.cdll.LoadLibrary(libc_pos)


def return_types():
    strchr = libc.strchr
    print(strchr(b"abcdef", ord("d")))
    strchr.restype = ctypes.c_char_p
    print(strchr(b"abcdef", ord("d")))


def arg_types():
    printf = libc.printf
    printf(b"An int %d, a double %f\n", 1234, ctypes.c_double(3.14))
    # printf(b"An int %d, a double %f\n", 1234, 3.14)
    printf.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_double]
    printf(b"An int %d, a double %f\n", 1234, 3.14)


def buffer():
    sprintf = libc.sprintf
    sprintf.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_double,
    ]
    buf = b''
    ret = sprintf(buf, b"An int %d, a double %f\n", 1234, 3.14)
    print('return:', ret, 'buffer:', buf)
    buf = ctypes.create_string_buffer(b'', 48)
    ret = sprintf(buf, b"An int %d, a double %f\n", 1234, 3.14)
    print('return:', ret, 'buffer:', buf.value, buf.raw)

    try:
        snprintf = libc.snprintf
    except AttributeError:
        snprintf = libc._snprintf

    snprintf.argtypes = [
        ctypes.c_char_p,
        ctypes.c_size_t,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_double,
    ]
    buf = ctypes.create_string_buffer(b'', 10)
    ret = snprintf(
        buf, ctypes.sizeof(buf), b"An int %d, a double %f\n", 1234, 3.14
    )
    print('return:', ret, 'buffer:', buf.value, buf.raw)


if __name__ == '__main__':
    return_types()
    arg_types()
    buffer()
