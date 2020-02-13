#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : ${FILE_NAME}
@Time    : 2020-02-11  20:59:06
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.register import RegisterPage


class LoginPage(BasePage):

    def goto_register(self):
        self.find(By.LINK_TEXT, "企业注册").click()
        return RegisterPage(self._driver)