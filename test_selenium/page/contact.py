#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : contact.py
@Time    : 2020-02-13  11:39:40
@Author  : indeyo_lin
"""
from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.main import MainPage


class ContactPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self, name, id, phone):
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member').click()
        self.find(By.ID, 'username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(id)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.LINK_TEXT, '保存').click()
        # self.find(By.LINK_TEXT, '离开此页')  # 有时候会弹出一个弹窗：成员的资料尚未保存，确定要离开吗？
        return self

    def goto_main(self):
        self.find(By.LINK_TEXT, '首页').click()
        # 刷新当前页面，获取最新的消息
        self._driver.execute_script("return location.reload()")
        sleep(3)
        return MainPage(self._driver)