# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : market.py
@Time    : 2020-04-02  10:42:54
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage
from test_appium.page.search import SearchPage


class MarketPage(BasePage):
    _search_locator = (By.ID, "action_search")
    _stocks_selector = (By.ID, "portfolio_stockName")

    def goto_search_from_top(self):
        self.find(self._search_locator).click()
        return SearchPage(self._driver)

    def goto_search_from_bottom(self):
        pass

    def goto_message(self):
        pass

    def get_stocks(self):
        return self.find_elements_and_get_text(self._stocks_selector)

    def get_sh_and_sz_stocks(self):
        pass

    def get_hk_stocks(self):
        pass

    def goto_market(self):
        pass

    def add_stocks_quick(self):
        pass
