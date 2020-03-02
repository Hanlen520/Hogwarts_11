#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : demo.py
@Time    : 2020-02-23  22:04:19
@UpdateTime: 2020-03-02 08:26:00
@Author  : indeyo_lin
"""

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("tencent")
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/tv_left")
el6.click()

driver.quit()