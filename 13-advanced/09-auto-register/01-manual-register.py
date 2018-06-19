# -*- encoding: utf-8 -*-
from registry import register, ls


class CommandA:
    pass


register(CommandA)
ls()
