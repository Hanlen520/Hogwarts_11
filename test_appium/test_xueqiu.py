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
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
            "androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]")
        el4.click()
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
        el5.click()
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_left")
        el6.click()

    def test_search_alibaba_and_get_price_from_hk(self):
        """
        20200216作业2
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

    def test_add_stock(self):
        """
        20200216作业3
        添加某只股票到自选，然后再次搜索并验证，股票已经加入自选。（不要使用文字内容判断，使用get attribute）
        :return: 
        """
        # self.driver.find_element(By.XPATH, '//*[contains(@resource-id = "tv_search")]').click()
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, '//*[@text="BABA"]').click()
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        self.driver.find_element(By.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id,"add_attention")]').click()
        self.driver.find_element(By.ID, 'action_close').click()
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, '//*[@text="BABA"]').click()
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        # 通过“已添加”的resource-id属性“followed_btn”定位到该元素，再通过get_attribute获取到text属性，断言text属性是否等于”已添加“
        # 这么做可能会有2个问题
        # 1. 假如没有添加成功，定位“followed_btn”的时候一定会报错
        # 2. 假如添加成功，但是按钮的text改变，也会断言失败
        # 所以最好的做法是：通过层级关系获取该按钮的父元素，再取子元素，再通过get_attribute获取resource-id属性，判断是否等于"followed_btn"。
        # followed_button = self.driver.find_element(
        #     By.XPATH,
        #     '//*[@text="09988"]/../../..//*[contains(@resource-id,"add_attention")]//*[contains(@class,"TextView")]'
        # )
        # assert "followed_btn" in followed_button.get_attribute('resource-id')
        # 受思寒大佬启发，直接用follow来定位按钮，这个定位方法简洁很多，学习了！
        followed_button = self.driver.find_element(
            By.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"follow")]')
        assert "已添加" in followed_button.get_attribute('text')

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

    def test_page_source(self):
        print(self.driver.page_source)

    def teardown(self):
        sleep(20)
        # self.driver.quit()
