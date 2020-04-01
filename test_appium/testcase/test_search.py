# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_search.py
@Time    : 2020-03-30  10:30:18
@Author  : indeyo_lin
"""
import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.page = App().start().main()

    def test_search(self):
        price = self.page.goto_search().search("alibaba").get_price("BABA")
        assert price < 200

    @pytest.mark.parametrize("stock, stock_type, price", [
        ("alibaba", "BABA", 200),
        ("JD", "JD", 20)
    ])
    def test_search_type(self, stock, stock_type, price):
        assert self.page.goto_search().search(stock).get_price(stock_type) > price

    def test_add_stock(self):
        assert "已添加" in self.page.goto_search().search("alibaba").add_stock().get_msg()