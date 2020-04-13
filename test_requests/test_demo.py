# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : test_demo.py
@Time    : 2020-04-12  13:02:11
@Author  : indeyo_lin
"""
from pprint import pprint

import requests
from requests import Session

proxies = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888"
}
url_get = "https://httpbin.testing-studio.com/get"

class TestRequests:
    def test_get(self):
        # get方法可以在url后面添加参数
        # r = requests.get("https://httpbin.testing-studio.com/get?a=1&b=2")
        # 和上面这种方法效果是一样的
        r = requests.get(
            "https://httpbin.testing-studio.com/get",
            params={
                "a": "1",
                "b": "2"
            },
            # 没有传递，可能是不支持
            data={
                "llll": "222222"
            }
        )

        print(r.text)
        print(r.content)
        print(r.json())
        assert r.status_code == 200

    def test_post(self):
        r = requests.post(
            "https://httpbin.testing-studio.com/post",
            # 对应args字段，params相当于在url后面加字段
            params={
                "name": "123",
                "sex": "female"
            },
            # 对应form字段
            data={
                "a": "1",
                "b": "2"
            },
            # 不起作用
            json={
                "date": "20200413"
            },
            # 字段首字母会自动变成大写
            headers={"hello": "world"},
            cookies={"wjz": "2020"},
            proxies=proxies,
            verify=False
        )

        # print(r.text)
        # print(r.content)
        # 返回 urllib3.response.HTTPResponse object 对象
        # print(r.raw)
        pprint(r.json())
        assert r.status_code == 200
        assert "world" in r.json()["headers"]["Hello"]

    def test_upload(self):
        r = requests.post(
            "https://httpbin.testing-studio.com/post",
            files={"files": open("__init__.py", 'rb')},
            proxies=proxies,
            verify=False
        )

        print(r.text)
        assert r.status_code == 200

    def test_session(self):
        s = Session()
        s.proxies = proxies
        s.verify = False
        s.get(url_get)
        # todo: session暂时未跑通
        s.mount()

