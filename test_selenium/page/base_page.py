#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : base_page.py
@Time    : 2020-02-11  19:18:02
@Author  : indeyo_lin
"""
from selenium import webdriver


class BasePage:

    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)

            self.driver.get(self._base_url)
        else:
            self.driver = driver