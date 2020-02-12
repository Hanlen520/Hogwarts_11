#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : base_page.py
@Time    : 2020-02-11  19:18:02
@Author  : indeyo_lin
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):  # 如果不确定driver类型，则无法调用他的方法
        if driver is None:
            # 用于IndexPage进行初始化
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)

            self._driver.get(self._base_url)
        else:
            # 用于RegisterPage、LoginPage等页面的引用
            self._driver = driver

    def close(self):
        sleep(20)
        self._driver.quit()
