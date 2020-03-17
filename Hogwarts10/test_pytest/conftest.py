#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : Hogwarts10
@File    : conftest.py
@Time    : 2019-10-20  15:08:03
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

import pytest
import logging

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture(scope="module")
def login():
    logging.info("login before the module")


@pytest.fixture(scope="class")
def teardown_A():
    yield None
    logging.info("teardown class A")

@pytest.fixture()
def setup_B():
    logging.info("setup_B")

@pytest.fixture(params=[1, 2, 3])
def setup_B_6():
    return request.param  # NameError

@pytest.fixture(scope="module")
def teardown_module():
    logging.info("the module is over")