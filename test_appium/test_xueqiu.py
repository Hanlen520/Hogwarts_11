#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_xueqiu.py
@Time    : 2020-03-02  08:51:05
@Author  : indeyo_lin
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True  # 设置以后不会清空数据，再次进入app不会有协议同意的弹框
        caps["dontStopAppOnReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
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

    def test_search_alibaba_and_get_price_from_hk(self):
        """
        02020216作业2
        搜索股票，点击股票分类，选择香港上市的阿里巴巴股票（根据xpath，而不是顺序），断言股价大于200
        """
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("alibaba")
        self.driver.find_element(By.XPATH, "//*[@text='阿里巴巴']").click()
        price_element = (By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(price_element))
        assert float(self.driver.find_element(*price_element).text) > 200

    def test_scroll(self):
        size = self.driver.get_window_size()
        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
                .release() \
                .perform()

    def test_device(self):
        # self.driver.background_app(5)
        # todo: lock函数这里报错了WebDriverException，看看是怎么回事
        self.driver.lock(5)
        # self.driver.unlock()


    def teardown(self):
        sleep(20)
        # self.driver.quit()
