# Generated by Selenium IDE
from time import sleep

import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        pass
        # self.driver.quit()

    def test_test_hogwarts(self):
        self.driver.get("https://testerhome.com/")
        self.driver.set_window_size(1324, 689)
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
        self.driver.find_element(By.XPATH, '//div/div/div[2]/div/a').click()  # 定位符不对！获得的是一组元素
