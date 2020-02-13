#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : register.py
@Time    : 2020-02-11  15:32:39
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class RegisterPage(BasePage):

    def register(self, corp_name):
        self.find(By.ID, 'corp_name').send_keys(corp_name)
        self.find(By.ID, "iagree").click()
        self.find(By.ID, "submit_btn").click()
        return self   # 返回 RegisterPage 页面对象本身

    def get_js_error_msg(self):
        result = []  # 返回报错消息列表
        for error in self._driver.find_elements(By.CSS_SELECTOR, ".js_error_msg"):
            # find_elements可以取到所有匹配的元素
            result.append(error.text)

        return result
