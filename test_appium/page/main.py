# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : main.py
@Time    : 2020-03-30  10:06:20
@Author  : indeyo_lin
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.search import SearchPage


class MainPage(BasePage):

    def goto_search(self):
        self.find(MobileBy.ID, "tv_search").click()
        return SearchPage(self._driver)

    def goto_trade(self):
        pass

    def goto_profile(self):
        pass
