#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : index.py
@Time    : 2020-02-11  15:29:17
@Author  : indeyo_lin
"""

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.login import LoginPage
from test_selenium.page.register import RegisterPage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def go_to_register(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        return RegisterPage(self._driver)

    def go_to_login(self):
        self._driver.find_element(By.LINK_TEXT, "企业登录").click()
        return LoginPage(self._driver)


