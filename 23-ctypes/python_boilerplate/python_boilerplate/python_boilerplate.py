# -*- coding: utf-8 -*-

"""Main module."""

if __name__ == '__main__':
    from ctypes import cdll, c_char_p
    lib = cdll.LoadLibrary('Qt5Corexxx.dll')
    lib.qVersion.restype = c_char_p
    print('Qt version:', lib.qVersion().decode('ascii'))
