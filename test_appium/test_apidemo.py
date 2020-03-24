# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_apidemo.py
@Time    : 2020-03-23  19:43:20
@Author  : indeyo_lin
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestApiDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)


    def test_toast(self):
        scroll_to_element1 = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element1).click()

        scroll_to_element2 = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element2).click()
        # 方法1：XPATH定位
        # self.driver.find_element(By.XPATH, '//*[@text="Make a Popup!"]').click()
        # 方法2：accessibility_id定位，用的是content-desc属性
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(By.XPATH, '//*[@text="Search"]').click()
        # 这个办法看样子不行。。还得用xpath
        # print(self.driver.find_element(By.CLASS_NAME, "android.widget.Toast").text)
        # toast出现的时间比较短，所以最好保存下来
        toast = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        assert 'Clicked popup menu' in toast