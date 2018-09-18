# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:23:36 2018

@author: ying.zhang01
"""

import os


class Element:
    """常量元素类。

    相关文件的路径名称常量。

    Attributes:
        BASE_PATH: 项目路径目录
        CONFIG_FILE: 配置文件路径
        DATA_FILE: 数据文件路径
        LOG_DIR: 日志文件目录
        REPORT_DIR: 报告文件目录
    """

    BASE_PATH = os.path.split(os.path.split(
            os.path.dirname(os.path.abspath(__file__)))[0])[0]  # 项目路径目录
    CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.json')  # 配置文件路径
    DATA_FILE = os.path.join(BASE_PATH, 'data', 'testcase.xlsx')  # 数据文件路径
    LOG_DIR = os.path.join(BASE_PATH, 'log')  # 日志文件目录
    REPORT_DIR = os.path.join(BASE_PATH, 'report')  # 报告文件目录


if __name__ == '__main__':
    print(Element.BASE_PATH)
