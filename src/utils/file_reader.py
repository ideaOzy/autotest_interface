# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:23:23 2018

@author: ying.zhang01
"""

import os
import json
from pprint import pprint

import xlrd

from utils.log import Log


class ExcelReader:
    """excel读取类,返回list。"""

    def __init__(self, filepath):
        """初始化excel表读取类。

        Args:
            filepath: string--需要读取excel的文件路径
        """
        if os.path.exists(filepath):
            self.filepath = filepath
        else:
            raise FileNotFoundError('excel文件不存在!')
        self._data = None

    def get_case(self):
        """如果是第一次调用，读取excel中的测试用例，否则直接返回之前保存的数据。

        Returns:
            list；列表中的每项是一个字典，字典的内容是excel表中一条测试用例。例如：
            [
                {
                    'id': 1.0,
                    'name': '图灵api接口',
                    'url': 'http://www.tuling123.com/openapi/api',
                    'method': 'POST',
                    'params': '{}',
                    'expect_value': '{"code":40001,"text":"亲爱的，key不对哦。"}',
                    'key': 'dfeb1cc8125943d29764a2f2f5c33739'
                },
                {
                    'id': 2.0,
                    'name': '测试api2',
                    'url': 'http://10.8.85.6:8011/api/register/HelloWorld',
                    'method': 'GET',
                    'params': '{}',
                    'expect_value': '"Hello World! xxxxxxxxxx"',
                    'key': ''
                }
            ]

        Raises:
        """
        if self._data is None:
            all_case = []
            xlsx_object = xlrd.open_workbook(self.filepath)  # 打开xlsx
            me = xlsx_object.sheets()[0]  # 打开xlsx的第一个table
            nrows = me.nrows
            Log.info("读取测试用例...")
            # 遍历case
            for i in range(1, nrows):
                all_case.append({
                    "id": me.cell(i, 0).value,
                    'name': me.cell(i, 1).value,
                    'url': me.cell(i, 2).value,
                    'method': me.cell(i, 3).value,
                    'params': me.cell(i, 4).value,
                    'expect_value': me.cell(i, 5).value,
                    'key': me.cell(i, 6).value
                })

            Log.info("共读取 " + str(len(all_case)) + " 个测试用例。")
            Log.info("测试用例集合: " + str(all_case))
            self._data = all_case
        return self._data


class JsonReader:
    """json配置文件读取类。"""

    def __init__(self, filepath):
        """初始化excel表读取类。

        Args:
            filepath: string--需要读取excel的文件路径
        """
        if os.path.exists(filepath):
            self.filepath = filepath
        else:
            raise FileNotFoundError('json文件不存在!')
        self._data = None

    @property
    def data(self):
        """"""
        if self._data is None:
            with open(self.filepath, 'rb') as f:
                self._data = json.load(f)
        return self._data


if __name__ == '__main__':
    # config_path = "..\\..\\config\\config.json"
    # config = JsonReader(config_path).data
    # pprint(config)
    # print(config['name'])

    # testcase_path = "..\\..\\data\\testcase.xlsx"
    # testcase = ExcelReader(testcase_path).get_case()
    # pprint(testcase)
    data = {"name": 2, "email": 1}
    data1 = {"name": "zhangying",
             "email": "xx@163.com",
             "report": {"title": "xx",
                        "description": "6",
                        "tester": "6",
                        "verbosity": 2}
             }
    print(json.dumps(data))
    print(json.dumps(data1))
