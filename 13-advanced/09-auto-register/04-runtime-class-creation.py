# -*- encoding: utf-8 -*-
import registry


def new_command_cls(name):
    cls = type(
        name,
        (),
        {'run': lambda self: print('good')}
    )
    registry.register(cls)
    return cls


CommandA = new_command_cls('CommandA')
registry.ls()
CommandA().run()
