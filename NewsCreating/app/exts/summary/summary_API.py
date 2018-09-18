# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/7/23 16:18
# Author :  Richard
# File   :  summary_API.py

from __future__ import print_function

import codecs

from .abstract import Keyword, Sentence
from config import BASE_PATH


def summary_API():
    # try:
    #     reload(sys)
    #     # sys.setdefaultencoding('utf-8')
    # except:
    #     pass

    text = codecs.open(BASE_PATH+'\\app\\static\\summary_source.txt', 'r', 'utf-8').read()
    w = Keyword()
    w.analyze(text=text, lower=True, window=1)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    print( '关键词：' )
    for item in w.get_keywords(20, word_min_len=1):
       print(item.word, item.weight)

    print()
    print( '关键短语：' )
    for phrase in w.get_keyphrases(keywords_num=20, min_occur_num= 2):
        print(phrase)

    s = Sentence()
    s.analyze(text=text, lower=True, source = 'all_filters')

    print()
    print( '摘要：' )
    summary = ""
    for item in s.get_key_sentences(num=3):
        summary += item.sentence
        summary += '；'
        # print(item.index, item.weight, item.sentence)
        print(item.sentence)
    print("summary:{}。".format(summary))
    return summary

if __name__ == '__main__':
    summary_API()
