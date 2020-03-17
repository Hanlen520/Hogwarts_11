#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts10
@File    : test_requests_homework_1013.py
@Time    : 2019-10-13  15:59:51
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from jsonpath import jsonpath
from requests import get

"""
课间作业1
test_get_login() 发起get请求https://testerhome.com/api/v3/topics.json?limit=2 断言最后一条结果中的帖子的用户名是liangqiangWang
test_xueqiu_search 在雪球上发起股票搜索，搜索sogo股票，断言结果中有名字为“搜狗”的股票
"""


def test_get_login():
    url = 'https://testerhome.com/api/v3/topics.json'
    repr = get(url, params={'limit': '2'}).json()
    assert repr['topics'][-1]['user']['name'] == 'liangqiangWang'
    # assert jsonpath(repr, "$.topics[-1:][(?@.name)]") == 'liangqiangWang'  #jsonpath没跑起来


def test_xueqiu_search():
    url = 'http://xueqiu.com/stock/search.json'
    params = {"code": "%E6%90%9C%E7%8B%97", "size": "3", "page": "1"}
    header = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    cookie = {
        "aliyungf_tc": "AQAAAMu7ii8b7wUAQrV0cW9CCi+DXKPA"
    }
    repr = get(url, params=params, header=header, cookies=cookie).content  # 调用json提示JSONDecodeError
    print(repr)


"""
课后作业2
企业微信的接口初步熟悉

api介绍 https://work.weixin.qq.com/api/doc#90000/90135/91039
test_get_token 使用requests发送get请求，从企业微信的响应中获取access_token
"""


def test_get_login():
    url = ' https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    param = {"corpid": "ID", "corpsecret": "SECRET"}
    print(get(url, params=param).json())
