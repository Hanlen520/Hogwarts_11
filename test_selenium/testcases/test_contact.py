#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_contact.py
@Time    : 2020-02-13  11:45:38
@Author  : indeyo_lin
"""
from time import time

from test_selenium.page.contact import ContactPage


class TestContact:

    def setup(self):
        self.contact = ContactPage(mode="reuse")

    def test_add_member(self):
        # 作业2：添加用户
        # 方法2：先获取消息条数 n ，再取 id 属性为 2n-1 的消息，判断 text 中是否包含 姓名
        name = "NO"+str(int(time()))
        self.contact.add_member(name, name, "13800000000")
        assert name in self.contact.goto_main().get_message()

    def test_edit_member(self):
        self.contact.edit_member()

    def test_goto_main(self):
        self.contact.goto_main()

    def teardown(self):
        self.contact.close()