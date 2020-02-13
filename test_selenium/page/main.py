#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : main.py
@Time    : 2020-02-09  16:07:08
@Author  : indeyo_lin
"""
from selenium import webdriver

from test_selenium.page.base_page import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"


