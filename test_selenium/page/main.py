#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : main.py
@Time    : 2020-02-09  16:07:08
@Author  : indeyo_lin
"""

from test_selenium.page.base_page import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def get_message(self):
        # 另外一种方案：先获取消息条数 n ，再取 id 属性为 2n-1 的消息，返回标签span的text信息
        return self._driver.execute_script(
            'return document.querySelector("a.js_todo_item > div > span.index_message_item_main_desc")'
            '.getAttribute("title");')

