# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : app.py
@Time    : 2020-03-30  10:07:34
@Author  : indeyo_lin
"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main import MainPage


class App(BasePage):
    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"

    def start(self):
        # 如果app未启动，则初始化driver
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            # 类变量可以给所有实例对象调用
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity
            caps["noReset"] = True  # 设置以后不会清空数据，再次进入app不会有协议同意的弹框
            # 暂时注释掉下面两个加速器，为了避免出现A new session could not be created.这个问题
            caps["dontStopAppOnReset"] = True  # True则不会重启app
            # caps["skipDeviceInitialization"] = True
            # webview测试，需要chromedriver和chrome版本匹配
            caps["chromedriverExecutable"] = "F:\chromedriver_win32_2.20\chromedriver.exe"
            # Genymotion 模拟器的udid会变，尽量不写死，或者看看能不能给设备固定一个名字
            # caps["udid"] = "192.168.210.101:5555"

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            # 如果app启动过，则只需要重启app，而不需要重启appium整个流程，节约时间
            self._driver.start_activity(self._appPackage, self._appActivity)

            # todo: 为什么不直接return MainPage()呢？？
            # return MainPage(self._driver)
        return self

    # 这里单独定义一个函数，和在start里面直接返回，有什么区别吗？
    # 有区别。可以对启动过程首页的一些加载问题做处理
    def main(self):
        # until 的入参需要传入一个函数名，且带有driver参数
        def wait_load(driver):
            source = self._driver.page_source
            # 如果页面出现tab我的，则说明首页加载完成
            if '我的' in source:
                return True

        # 传入函数名，运行时调用
        WebDriverWait(self._driver, 60).until(wait_load)
        return MainPage(self._driver)
