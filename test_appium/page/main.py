# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : main.py
@Time    : 2020-03-30  10:06:20
@Author  : indeyo_lin
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.market import MarketPage
from test_appium.page.search import SearchPage


class MainPage(BasePage):
    _search_locator = (MobileBy.ID, "tv_search")

    def goto_search(self):
        self.find(self._search_locator).click()
        return SearchPage(self._driver)

    def goto_market(self):
        self.find_by_text("行情").click()
        return MarketPage(self._driver)

    def goto_trade(self):
        pass

    def goto_profile(self):
        pass
