#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : ${FILE_NAME}
@Time    : 2020-02-12  11:23:41
@Author  : indeyo_lin
"""
from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class MaterialPage(BasePage):

    def add_text(self):
        pass

    def goto_image(self):
        self.find(By.CSS_SELECTOR, "#profile_navigation li:nth-child(3)").click()
        return self

    def add_image(self, image_path):
        self.find(By.CSS_SELECTOR, ".js_upload_file_selector").click()
        self.find(By.ID, "js_upload_input").send_keys(image_path)
        sleep(5)  # 等待图片上传完再点击确认按钮
        self.find(By.CSS_SELECTOR, "[d_ck=submit]").click()
        return self

    def get_image_total(self):
        return self.find(By.CSS_SELECTOR, ".js_list_total").text