# -*- coding: UTF-8 -*-

# class GlobalVar():
    # def __init__(self):
    #     self.register_is = False
    #
    # def getregister(self):
    #     return self.register_is
    #
    # def setregister(self, value):
    #     self.register_is = value

def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue


