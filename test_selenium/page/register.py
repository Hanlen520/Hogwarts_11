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
        self.driver.find_element(By.ID, 'corp_name').send_keys(corp_name)
        self.driver.find_element(By.ID, "iagree").click()
        self.driver.find_element(By.ID, "submit_btn").click()


