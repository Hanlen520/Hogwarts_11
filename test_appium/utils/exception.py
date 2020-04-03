# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : exception.py
@Time    : 2020-04-03  09:54:55
@Author  : indeyo_lin
"""
import logging

logging.basicConfig(level=logging.INFO)


def exception_handle(func):
    def magic(*args, **kwargs):
        from test_appium.page.base_page import BasePage
        # 获取BasePage实例对象的参数self，这样可以复用driver
        _self: BasePage = args[0]
        try:
            # logging.info('error count is %s' % _self._error_count)
            result = func(*args, **kwargs)
            _self._error_count = 0
            # 返回调用函数本身，要不然返回值会被装饰器吃掉
            return result
        # 弹窗等异常处理逻辑
        except Exception as e:
            # 如果超过最大异常处理次数，则抛出异常
            if _self._error_count > _self._error_max:
                raise e
            _self._error_count += 1
            for element in _self._black_list:
                # 用find_elements，就算找不到元素也不会报错
                elements = _self._driver.find_elements(*element)
                logging.info(element)
                # 是否找到弹窗
                if len(elements) > 0:
                    # 出现弹窗，点击掉
                    elements[0].click()
                    # 弹窗点掉后，重新查找目标元素
                    return magic(*args, **kwargs)
            # 弹窗也没有出现，则抛出异常
            logging.warning("no error is found")
            raise e

    return magic
