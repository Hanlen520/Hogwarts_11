# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : search.py
@Time    : 2020-03-30  10:07:23
@Author  : indeyo_lin
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class SearchPage(BasePage):

    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(By.XPATH, "//*[@text='阿里巴巴']").click()
        return self

    def get_price(self, key: str) -> float:
        # todo:获取股票价格参数化
        price_element = (By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")
        # WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of_element_located(price_element))
        return float(self.find(*price_element).text)
