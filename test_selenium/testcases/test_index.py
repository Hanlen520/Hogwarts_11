#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_index.py
@Time    : 2020-02-11  15:45:08
@Author  : indeyo_lin
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.index import IndexPage
from test_selenium.page.register import RegisterPage


class TestIndex:

    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/")

    def test_register(self):

        # self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # self.driver.find_element(By.ID, 'corp_name').send_keys("才华有限公司")
        # self.driver.find_element(By.ID, "iagree").click()
        # self.driver.find_element(By.ID, "submit_btn").click()

        page = IndexPage(self.driver)
        page.go_to_register().register("才华有限公司")


    def teardown(self):
        sleep(30)
        self.driver.quit()