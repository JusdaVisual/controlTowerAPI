

# -*- coding: utf-8 -*-
#  全局变量公用类


"""
初始化
"""
def _init():
    global _global_dict
    _global_dict = {}



""" 
定义一个全局变量，并赋值
"""
def set_value(name,value):
    _global_dict[name] = value

"""
获取全局变量的值,不存在则返回None
"""
def get_value(name,value=None):
    try:
        return _global_dict[name]
    except KeyError:
        return value

