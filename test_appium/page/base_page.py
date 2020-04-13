# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : base_page.py
@Time    : 2020-03-30  10:07:52
@Author  : indeyo_lin
"""
import logging

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.utils.exception import exception_handle


class BasePage:
    # 用类型提示，方便使用driver方法
    _driver: WebDriver
    # 黑名单，异常处理的定位符列表
    _black_list = [
        (By.ID, "image_cancel"),
        (By.ID, "tv_agree"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
        (By.ID, "ib_close")
    ]
    # 最大异常处理次数
    _error_max = 10
    # 异常处理计数器
    _error_count = 0
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @exception_handle
    def find(self, locator, key=None):
        logging.info(locator)
        logging.info(key)
        # 定位符支持元组格式和两个参数格式
        locator = locator if isinstance(locator, tuple) else (locator, key)
        # done：显示等待有点尴尬，不知道放哪里比较好。
        #  放在find_element前面，出现弹窗的时候，异常处理拦截不到直接超时异常了
        #  放在后面，真正需要用到显示等待的时候，被异常处理拦截
        # 这个问题解决了！原来问题在于异常处理函数没写对，异常处理完不应该返回函数本身，而是要返回magic()
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        element = self._driver.find_element(*locator)
        return element

    @exception_handle
    def find_and_get_text(self, locator, key=None):
        logging.info(locator)
        logging.info(key)
        # 定位符支持元组格式和两个参数格式
        locator = locator if isinstance(locator, tuple) else (locator, key)
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        element = self._driver.find_element(*locator)
        logging.info(element.text)
        return element.text

    @exception_handle
    def find_elements_and_get_text(self, locator, key=None):
        logging.info(locator)
        logging.info(key)
        # 定位符支持元组格式和两个参数格式
        locator = locator if isinstance(locator, tuple) else (locator, key)
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        elements = self._driver.find_elements(*locator)
        texts = []
        for element in elements:
            texts.append(element.text)
        logging.info(texts)
        return texts

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        # 这里可以复用find的异常处理逻辑
        return self.find(self.text(key))

    def get_toast(self):
        return self._driver.find_element(By.XPATH, "//[@class='android.widget.Toast']").text
