#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : manage_tools.py
@Time    : 2020-02-12  11:20:46
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.material import MaterialPage


class ManageToolsPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def go_to_material(self):
        self._driver.find_element(By.CSS_SELECTOR, ".manageTools_cnt_items li:nth-child(5)").click()  # 这里有个巨坑，用LINK_TEXT过不去的
        return MaterialPage(self._driver)