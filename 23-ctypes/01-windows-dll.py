# -*- encoding: utf-8 -*-
# https://docs.microsoft.com/en-us/windows/desktop/LearnWin32/working-with-strings
# https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-messageboxw
import ctypes
import ctypes.wintypes

MB_ICONWARNING = 0x30
MB_CANCELTRYCONTINUE = 0x06
MB_DEFBUTTON2 = 0x100


def basic_invocation():
    user32 = ctypes.windll.user32
    print(user32)
    print(user32.MessageBoxW)
    ret = user32.MessageBoxW(
        None,
        ctypes.wintypes.LPCWSTR("Resource not available\nDo you want to try again?"),
        ctypes.wintypes.LPCWSTR("Account Details"),
        # "Account Details",
        ctypes.c_uint(MB_ICONWARNING | MB_CANCELTRYCONTINUE | MB_DEFBUTTON2)
    )
    print(ret)


def use_wrapper():
    prototype = ctypes.WINFUNCTYPE(
        ctypes.c_int,
        ctypes.wintypes.HWND, ctypes.wintypes.LPCWSTR, ctypes.wintypes.LPCWSTR, ctypes.wintypes.UINT
    )
    paramflags = (
        (1, "hwnd", None),
        (1, "text", "Hi"),
        (1, "caption", "Hello from ctypes"),
        (1, "flags", MB_ICONWARNING | MB_CANCELTRYCONTINUE | MB_DEFBUTTON2)
    )
    MessageBox = prototype(("MessageBoxW", ctypes.windll.user32), paramflags)
    MessageBox(text='中文提示', caption='调用windows函数')


if __name__ == '__main__':
    basic_invocation()
    use_wrapper()
