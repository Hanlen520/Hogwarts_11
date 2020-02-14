#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_main.py
@Time    : 2020-02-14  10:53:46
@Author  : indeyo_lin
"""
from test_selenium.page.main import MainPage


class TestMain:

    def setup(self):
        self.main = MainPage(mode="reuse")

    def test_get_message(self):
        print(self.main.get_message())
        assert "管理员" in self.main.get_message()
