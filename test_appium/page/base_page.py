# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : base_page.py
@Time    : 2020-03-30  10:07:52
@Author  : indeyo_lin
"""
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, key=None):
        if key is None:
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, key)

