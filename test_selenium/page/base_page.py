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

    def __init__(self, driver: WebDriver = None, mode=None):  # 如果不确定driver类型，则无法调用他的方法
        if driver is None:
            if mode == "reuse":
                options = webdriver.ChromeOptions()
                # Chrome --remote-debugging-port=9222
                options.debugger_address = "127.0.0.1:9222"  # 复用已有浏览器
                self._driver = webdriver.Chrome(options=options)
            else:
                # 用于IndexPage进行初始化
                self._driver = webdriver.Chrome()

            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
        else:
            # 用于RegisterPage、LoginPage等页面的引用
            self._driver = driver

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)


    def close(self):
        sleep(20)
        self._driver.quit()
