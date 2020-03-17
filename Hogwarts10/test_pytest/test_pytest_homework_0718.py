#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : Hogwarts10
@File    : test_pytest_homework_0718.py
@Time    : 2019-10-16  21:55:27
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
https://testerhome.com/topics/19921
课后作业
实现一个测试用例集合，包含3个类TestA TestB TestC，每个类包含三个方法，总共9个方法 test_1 到test_9。执行顺序的时候，希望完成如下的顺序
顺序控制

logging.info("login")
TestA
TestA teardown完成环境清理
TestB每个方法都要有初始化，但是没有teardown
TestB的test6包含3个参数化用例
TestC的执行顺序是test8 test9 test7
整个module完成执行数据清理
完成特定动作只需要用loggin打log表示即可，最后贴出如下内容

整个module的源代码
allure执行的报告截图
"""

import pytest
import logging

logging.basicConfig(level=logging.DEBUG)

def teardown_module():
    logging.info("teardown module")

class TestA:

    @classmethod
    def setup_class(cls):
        logging.info("login")

    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert [2, 3] == [3, 2]

    def test_3(self):
        assert 1 == None

    @classmethod
    def teardown_class(cls):
        logging.info("teardown")


class TestB:

    def setup_method(self):
        logging.info("setup_B")

    def test_4(self):
        assert "gogo" == "gogo"

    def test_5(self):
        assert {"a" : 3 , "b" : 1} == {"a" : 3 , "b" : 2}

    @pytest.mark.parametrize("input, expected",[(4 + 3, 8), (5 + 7, 12), (2 + 2, 5)])
    def test_6(self, input, expected):
        assert input == expected

class TestC:

    @pytest.mark.run(order=2)
    def test_7(self):
        assert False

    @pytest.mark.run(order=1)
    def test_8(self):
        assert 1 == "1"

    @pytest.mark.run(order=3)
    def test_9(self):
        assert True