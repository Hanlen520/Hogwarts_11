#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_testerhome_homework.py
@Time    : 2019-12-31  07:38:55
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTesterhome:

    def setup_method(self):
        browser = os.getenv("browser", "").lower()
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        self.driver.get('http://testerhome.com')
        # 隐式等待
        self.driver.implicitly_wait(2)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def teardown_method(self):
        sleep(20)
        self.driver.quit()

    def test_hogwarts(self):
        """
        课间作业1
        进入testerhome，访问社团，访问霍格沃兹测试学院，访问最顶部的第一个帖子

        """
        self.driver.set_window_size(2000, 1000)
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # 显示等待
        # element = (By.LINK_TEXT, '霍格沃兹测试学院')
        element = (By.CSS_SELECTOR, '[data-name=霍格沃兹测试学院]')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.CSS_SELECTOR, ".panel-body>div:nth-child(1) .title").click()

    def test_mtsc2020_homewrok2(self):
        """
        课间作业2
        进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围
        """
        self.driver.find_element_by_partial_link_text('MTSC2020').click()
        self.driver.find_element_by_css_selector('.toc-container>button').click()
        element = (By.CSS_SELECTOR, '.list-container li:nth-child(4) a')
        self.wait(10, expected_conditions.element_to_be_clickable(element))  # 什么是定位符？一定是这样的元组格式吗？
        self.driver.find_element(*element).click()

    def test_jinshuju(self):
        """
        frame的切换，由于问卷已经关闭，代码未运行
        :return:
        """
        self.driver.get("https://testerhome.com/topics/21495")
        commit = (By.CSS_SELECTOR, '.published-form__submit')

        self.driver.switch_to.frame()
        self.wait(10, expected_conditions.element_to_be_clickable(commit))
        self.driver.find_element(*commit).click()

    def test_mtsc2020(self):
        """
        windows窗体切换
        :return:
        """
        self.driver.get("https://testerhome.com/topics/21805")
        element = (By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会")
        self.wait(5, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        print(self.driver.window_handles)
        self.driver.find_element(By.LINK_TEXT, '演讲申请').click()
        self.driver.execute_script()

    def test_js(self):
        for code in [
            'return document.title',
            'return document.querySelector(".active").className',
            'return performance.timing'
        ]:
            result = self.driver.execute_script(code)
            print(result)
