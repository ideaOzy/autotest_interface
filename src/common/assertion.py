# -*- coding: utf-8 -*-
"""
Created on 2018/9/7 17:44

@author: ying.zhang01

该模块添加各种自定义断言，断言失败都抛出AssertionError异常即可。
"""


def assert_response(expect, fact):
    """自定义http响应结果断言。"""
    if expect != fact:
        raise AssertionError("-----执行结果: 预期和实际的不一致-----")
