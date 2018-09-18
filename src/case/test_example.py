# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:38:05 2018

@author: ying.zhang01
"""

import unittest
import json

from ddt import ddt, data

from common.http_request import HttpRequest
from utils.log import Log
from utils.file_reader import ExcelReader
from common.element_enum import Element
from common.assertion import assert_response


# 测试用例文档地址
# testcase_path = "..\\..\\data\\testcase.xlsx"
# 读取测试用例
# data_test = get_case(testcase_path)
data_test = ExcelReader(Element.DATA_FILE).get_case()


@ddt
class MyTest(unittest.TestCase):
    """本组测试用例标题。

    数据驱动测试（Data-Driven Tests），利用DDT来实现测试数据的参数化，
    做到数据与代码分离。
    """

    def setUp(self):
        """每个测试用例运行前环境准备。"""
        Log.info('------------测试用例运行开始-----------')

    def tearDown(self):
        """每个测试用例运行后环境清理。"""
        Log.info('------------测试用例运行结束-----------')

    @data(*data_test)
    def test_api(self, data_test):
        """DDT驱动的测试用例方法。"""
        # 接口请求参数
        Log.info('接口说明: %s' % (data_test['name']))
        Log.info('请求url: %s' % (data_test['url']))
        Log.info('请求参数: %s' % data_test['params'])
        Log.info('请求方式: %s' % data_test['method'])
        Log.info('请求期望值: %s' % data_test['expect_value'])
        # 测试用例接口请求
        api_req = HttpRequest(
                url=data_test['url'],
                method=data_test['method'],
                params=data_test['params']
                )
        api_res = api_req.get_response()
        # 输出接口请求结果
        Log.info("响应结果: %s" % api_res)

        # 断言判断期望值与实际值
        expect = json.loads(data_test['expect_value'])
        # Log.info(expect)
        fact = json.loads(api_res)
        # Log.info(fact)
        assert_response(expect, fact)
