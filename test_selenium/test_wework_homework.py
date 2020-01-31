#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_wework_homework.py
@Time    : 2020-01-15  07:44:10
@Author  : indeyo_lin
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Webdriver(object):
    pass


class TestWeWork:

    def setup(self):
        options = webdriver.ChromeOptions()
        options.debugger_address = "127.0.0.1:9222"  # 复用已有浏览器
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_add_member(self):
        """
        selenium课间作业3
        企业微信自动添加成员，需要复用已经登录的chrome，需要debugger address
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        element_add = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member')
        self.wait(10, expected_conditions.element_to_be_clickable(element_add))
        self.driver.find_element(*element_add).click()
        element_name = (By.ID, 'username')
        self.wait(10, expected_conditions.element_to_be_clickable(element_name))
        self.driver.find_element(*element_name).send_keys('Emma1')
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys('Emma1')
        self.driver.find_element(By.ID, 'memberAdd_mail').send_keys('emma1@163.com')
        self.driver.find_element(By.LINK_TEXT, '保存并继续添加').click()  # 奇怪，页面有两个相同元素，居然不会报错？


