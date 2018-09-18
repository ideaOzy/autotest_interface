# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:08:52 2018

@author: ying.zhang01
"""

from common.element_enum import Element
from utils.file_reader import JsonReader


class Config:
    """配置读取类。"""

    def __init__(self, config=Element.CONFIG_FILE):
        """初始化excel表读取类。

        Args:
            config: string--需要读取的json配置文件的路径。
        """
        self.config = JsonReader(config).data

    def get(self, element):
        """根据key名称获取配置文件中相应的数据。

        Args:
            element: string--json配置文件的key名称。
        """
        return self.config[element]


if __name__ == '__main__':
    config = Config()
    print(config.get('report')["title"])
