#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_xueqiu.py
@Time    : 2020-03-02  08:51:05
@Author  : indeyo_lin
"""
from appium import webdriver


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("tencent")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]")
        el4.click()
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
        el5.click()
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_left")
        el6.click()

    def teardown(self):
        self.driver.quit()