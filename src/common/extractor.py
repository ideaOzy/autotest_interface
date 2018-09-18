# -*- coding: utf-8 -*-

"""
抽取器，从响应结果中抽取部分数据
~~~~~~~~~~~

@Time: 2018/9/10 13:50
@author: ying.zhang01
@File: extractor.py
"""

import json
import jmespath


class JMESPathExtractor:
    """用JEMSPath实现对json格式数据的简单抽取。"""

    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.loads(body))
        except Exception as e:
            raise ValueError("Invalid query", + query + ":" + str(e))


if __name__ == '__main__':
    jstr = '{"name": "zhangying", "email": {"server": "smtp.united-imaging.com","sender": "softtester@united-imaging.com","password": "xAcmQ3gg","receiver": ["ying.zhang01@united-imaging.com"],"title": "自动化接口测试框架-测试邮件"},"report": {"title": "xx测试报告","description": "用例执行情况：","tester": "张颖","verbosity": 2}}'
    j = JMESPathExtractor()
    j1 = j.extract(query='email', body=jstr)
    print(j1)
