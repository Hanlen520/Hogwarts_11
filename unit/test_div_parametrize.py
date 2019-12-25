#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_div_parametrize.py
@Time    : 2019-12-25  07:34:54
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
import os.path
import pytest
import yaml

from utils.div import div


class TestDiv:

    @pytest.mark.parametrize("a, b, c", [
        (100, 10, 10),
        (0, 100, 0),
        (999999999, 3, 333333333)
    ])
    def test_int(self, a, b, c):
        assert div(a, b) == c

    @pytest.mark.parametrize("a, b, c", yaml.load(open(os.path.join(os.path.dirname(__file__), 'div.yaml'), 'r')))
    def test_float(self, a, b, c):
        print(yaml.load(open(os.path.join(os.path.dirname(__file__), 'div.yaml'), 'r')))
        assert div(a, b) == c

    def test_zero(self):
        with pytest.raises(ZeroDivisionError):
            div(10, 0)

    @pytest.mark.parametrize("a, b", [
        ('', 1),
        (1, '')
    ])
    def test_null(self, a, b):
        with pytest.raises(TypeError):
            div()

    @pytest.mark.parametrize("a, b", [
        ('0', 1),
        ('66', '11'),
        (10, '10')
    ])
    def test_string(self, a, b):
        with pytest.raises(TypeError):
            div(a, b)
