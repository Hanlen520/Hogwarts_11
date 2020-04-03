# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_decorator.py
@Time    : 2020-04-03  14:04:35
@Author  : indeyo_lin
"""
from unittest.test.testmock.testpatch import function


def say_hi(func):
    def magic(*args, **kwargs):
        print("Welcome to Hogwarts")
        # 还是func 本身
        print('the function name is %s' % func.__name__)
        return func(*args, **kwargs)
        # return 'Hello from magic'

    return magic


@say_hi
def welcome():
    # 变成了magic
    print(welcome.__name__)
    # 啊。。。这个被magic覆盖了
    return 'Hello from welcome'


def test_welcome():
    print(welcome())
