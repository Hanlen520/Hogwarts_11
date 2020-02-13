#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_manage_tools.py
@Time    : 2020-02-12  11:41:49
@Author  : indeyo_lin
"""
from test_selenium.page.manage_tools import ManageToolsPage


class TestManageTools:

    def setup(self):
        self.manage_tools = ManageToolsPage(mode="reuse")

    def test_add_image(self):
        # PO作业一：
        # 管理工具 -> 素材库 -> 图片 -> 上传
        image_page = self.manage_tools.go_to_material().go_to_image()
        image_num_old = image_page.get_image_total()
        image_page.add_image("D:\\project\\Hogwarts_11\\test_selenium\\page\\beautiful_sky.png")
        image_num_new = image_page.get_image_total()
        assert image_num_new > image_num_old

