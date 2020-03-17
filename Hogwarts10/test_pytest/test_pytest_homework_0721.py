#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : Hogwarts10
@File    : test_pytest_homework_0721.py
@Time    : 2019-10-20  14:49:30
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
把上一节课的作业用fixture替换，利用fixture完成setup与teardown的替换，参数化使用fixture替换

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

class TestA:

    def test_1(self,login):
        assert 1 == 1

    def test_2(self,login):
        assert [2, 3] == [3, 2]

    def test_3(self,teardown_A):
        assert 1 == None

class TestB:

    def test_4(self, setup_B):
        assert "gogo" == "gogo"

    def test_5(self, setup_B):
        assert {"a" : 3 , "b" : 1} == {"a" : 3 , "b" : 2}

    def test_6(self, setup_B_6):
        assert setup_B_6 == 2

class TestC:

    @pytest.mark.run(order=2)
    def test_7(self):
        assert False

    @pytest.mark.run(order=1)
    def test_8(self):
        assert 1 == "1"

    @pytest.mark.run(order=3)
    def test_9(self, teardown_module):
        assert True