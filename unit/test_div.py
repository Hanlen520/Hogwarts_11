#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_div.py
@Time    : 2019-12-22  15:50:24
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
from utils.div import div


class TestDiv1:

    def test_01(self):
        assert div(2, 1) == 2

    def test_02(self):
        assert div(1, 2) == 0.5

    def test_03(self):
        assert div(3.0, 1) == 3


