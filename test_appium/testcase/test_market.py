# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_market.py
@Time    : 2020-04-02  11:21:03
@Author  : indeyo_lin
"""
from test_appium.page.app import App


class TestMarket:
    def setup(self):
        self.market = App().start().main().goto_market()

    def test_search(self):
        # 作业1：进入行情页，搜索股票并添加自选，然后重新回到行情页
        # 添加自选前判断是否已添加，如果是，则先取消
        self.market.goto_search_from_top().search("ntes").check_if_selected().add_stock().close()
        assert "网易" in self.market.get_stocks()
