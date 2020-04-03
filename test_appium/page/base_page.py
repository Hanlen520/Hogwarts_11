# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : base_page.py
@Time    : 2020-03-30  10:07:52
@Author  : indeyo_lin
"""
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    def find(self, locator, key=None):
        logging.info(locator)
        logging.info(key)
        try:
            # 定位符支持元组格式和两个参数格式
            locator = locator if isinstance(locator, tuple) else (locator, key)
            WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
            element = self._driver.find_element(*locator)
            self._error_count = 0
            return element
            # if key is None:
            #     # 如果是元组格式，则需要将元组拆成两个参数
            #     element = self._driver.find_element(*locator)
            #     self._error_count = 0
            #     return element
            # else:
            #     element = self._driver.find_element(locator, key)
            #     self._error_count = 0
            #     return element
        # 弹窗等异常处理逻辑
        except Exception as e:
            # 如果超过最大异常处理次数，则抛出异常
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                # 用find_elements，就算找不到元素也不会报错
                elements = self._driver.find_elements(*element)
                logging.info(element)
                # 是否找到弹窗
                if len(elements) > 0:
                    # 出现弹窗，点击掉
                    elements[0].click()
                    # 弹窗点掉后，重新查找目标元素
                    return self.find(locator)
            # 弹窗也没有出现，则抛出异常
            logging.warning("no error is found")
            raise e

    def find_and_get_text(self, locator, key=None):
        logging.info(locator)
        logging.info(key)
        try:
            # 定位符支持元组格式和两个参数格式
            locator = locator if isinstance(locator, tuple) else (locator, key)
            WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
            element = self._driver.find_element(*locator)
            self._error_count = 0
            logging.info(element.text)
            return element.text
            # if key is None:
            #     # 如果是元组格式，则需要将元组拆成两个参数
            #     element = self._driver.find_element(*locator)
            #     self._error_count = 0
            #     return element
            # else:
            #     element = self._driver.find_element(locator, key)
            #     self._error_count = 0
            #     return element
        # 弹窗等异常处理逻辑
        except Exception as e:
            # 如果超过最大异常处理次数，则抛出异常
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                # 用find_elements，就算找不到元素也不会报错
                elements = self._driver.find_elements(*element)
                logging.info(element)
                # 是否找到弹窗
                if len(elements) > 0:
                    # 出现弹窗，点击掉
                    elements[0].click()
                    # 弹窗点掉后，重新查找目标元素
                    return self.find_and_get_text(locator)
            # 弹窗也没有出现，则抛出异常
            logging.warning("no error is found")
            raise e

    def find_elements_and_get_text(self, locator, key=None):
        logging.info(locator)
        logging.info(key)
        try:
            # 定位符支持元组格式和两个参数格式
            locator = locator if isinstance(locator, tuple) else (locator, key)
            WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
            elements = self._driver.find_elements(*locator)
            self._error_count = 0
            texts = []
            for element in elements:
                texts.append(element.text)
            logging.info(texts)
            return texts
            # if key is None:
            #     # 如果是元组格式，则需要将元组拆成两个参数
            #     element = self._driver.find_element(*locator)
            #     self._error_count = 0
            #     return element
            # else:
            #     element = self._driver.find_element(locator, key)
            #     self._error_count = 0
            #     return element
        # 弹窗等异常处理逻辑
        except Exception as e:
            # 如果超过最大异常处理次数，则抛出异常
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                # 用find_elements，就算找不到元素也不会报错
                elements = self._driver.find_elements(*element)
                logging.info(element)
                # 是否找到弹窗
                if len(elements) > 0:
                    # 出现弹窗，点击掉
                    elements[0].click()
                    # 弹窗点掉后，重新查找目标元素
                    return self.find(locator)
            # 弹窗也没有出现，则抛出异常
            logging.warning("no error is found")
            raise e

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        # 这里可以复用find的异常处理逻辑
        return self.find(self.text(key))

    def get_toast(self):
        return self._driver.find_element(By.XPATH, "//[@class='android.widget.Toast']").text