#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : index.py
@Time    : 2020-02-11  15:29:17
@Author  : indeyo_lin
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.register import RegisterPage


class IndexPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_register(self):
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        return RegisterPage(self.driver)