#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_testerhome_1.py
@Time    : 2019-12-31  07:38:55
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTesterhome:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://testerhome.com')
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        sleep(20)
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.set_window_size(2000, 1000)
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # 显示等待
        # element = (By.LINK_TEXT, '霍格沃兹测试学院')
        element = (By.CSS_SELECTOR, '[data-name=霍格沃兹测试学院]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.CSS_SELECTOR, ".panel-body>div:nth-child(1) .title").click()
