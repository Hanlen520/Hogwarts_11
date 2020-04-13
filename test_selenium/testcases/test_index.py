#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_index.py
@Time    : 2020-02-11  15:45:08
@Author  : indeyo_lin
"""

from test_selenium.page.index import IndexPage


class TestIndex:

    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        # self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # self.driver.find_element(By.ID, 'corp_name').send_keys("才华有限公司")
        # self.driver.find_element(By.ID, "iagree").click()
        # self.driver.find_element(By.ID, "submit_btn").click()

        self.index.goto_register().register("才华有限公司")

    def test_login_register(self):
        register_page = self.index.goto_login().goto_register().register("有钱花有限公司")
        # 这样做的好处是，假如没有写全字符串的全称，也可以匹配到
        assert "请填写" in "|".join(register_page.get_js_error_msg())

    def teardown(self):
        self.index.close()
