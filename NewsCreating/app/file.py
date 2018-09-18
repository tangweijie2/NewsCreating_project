# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/7/17 20:56
# Author :  Richard
# File   :  file.py

# import json
from bs4 import BeautifulSoup
import re

# 创建一个文件类，该实现了对基本文件类的扩展
class File():
    def __init__(self, file, access_mode='r'):
        # 利用传进来的文件初始化出一个基本的文件对象
        # 取得内容
        with open(file, access_mode) as file_object:
            self.content = file_object.read()  # 文件不大，所以直接读取所有字节到内存中
        # self.content = file_content
        # 判断内容是json格式还是XML格式, True代表json，False代表XML
        # if self.content[0] == '<':
        #     self.content_type = False
        # elif self.content[0] == '{':
        #     self.content_type = True
        # else:
        #     self.content_type = "格式错误"

    def parse_content(self):
        '''
        将文本内容解析为json或者XML对象
        :return json或XML对象:
        '''
        # return  "请求成功，这是一篇文章"
        return self.content
        # if self.content_type is True:
        #     return self.content  # 如果是json格式就直接返回
        # else:
        #     content_dict = {}
        #     print(self.content)
        #     soup = BeautifulSoup(self.content, "xml")  # 创建Beautiful对象
        #     all_tag = soup.find_all(name=re.compile("[a-z]+"))  # 过滤出所有的标签
        #     for tag in all_tag:
        #         if len(tag.attrs) == 0:
        #             content_dict[tag.name] = tag.string
        #         else:
        #             content_dict.update(tag.attrs)
        #     return content_dict

