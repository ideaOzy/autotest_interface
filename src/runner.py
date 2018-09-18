# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:53:12 2018

@author: ying.zhang01
"""

import os
import time
import unittest

from case.test_example import MyTest
from common.HTMLTestReportCN import HTMLTestRunner
from utils.config import Config
from common.element_enum import Element
from utils.log import Log
from utils.my_email import Email


if __name__ == '__main__':
    # 日志器
    Log.info('begin test...')
    # 配置文件读取
    config = Config()

    # 组织测试用例集
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))

    # 生成Html测试报告名字
    now = time.strftime("%Y-%m-%d %Hh_%Mm", time.localtime(time.time()))
    filename = os.path.join(Element.REPORT_DIR, now + "_report.html")

    # 使用HTMLTestRunner运行测试用例，并生成测试报告
    with open(filename, "wb") as fl:
        report = config.get("report")
        runner = HTMLTestRunner(
            stream=fl,
            title=report["title"],
            description=report["description"],
            tester=report["tester"],
            verbosity=report["verbosity"]
        )
        runner.run(suite)
    Log.info('end test.  run in ' + str(now))

    # 将测试报告发送到邮箱
    content = config.get("email")
    email = Email(server=content["server"],
                  sender=content["sender"],
                  password=content["password"],
                  receiver=content["receiver"],
                  title=content["title"],
                  message=Element.REPORT_DIR,
                  path=Element.DATA_FILE)
    # email.send()
