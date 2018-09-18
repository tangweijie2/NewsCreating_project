from __future__ import (absolute_import, division, print_function, unicode_literals)

from . import util
from .Segmentation import Segmentation


class Keyword(object):

    def __init__(self, stop_words_file=None,
                 allow_speech_tags=util.allow_speech_tags,
                 delimiters=util.sentence_delimiters):

        self.text = ''
        self.keywords = None

        self.seg = Segmentation(stop_words_file=stop_words_file,
                                allow_speech_tags=allow_speech_tags,
                                delimiters=delimiters)

        self.sentences = None
        self.words_no_filter = None  # 2维列表
        self.words_no_stop_words = None
        self.words_all_filters = None

    #分析文本
    def analyze(self, text,
                window=2,
                lower=False,
                vertex_source='all_filters',
                edge_source='no_stop_words',
                pagerank_config={'alpha': 0.85, }):
   

        # self.text = util.as_text(text)
        self.text = text
        self.word_index = {}
        self.index_word = {}
        self.keywords = []
        self.graph = None

        result = self.seg.segment(text=text, lower=lower)
        self.sentences = result.sentences
        self.words_no_filter = result.words_no_filter
        self.words_no_stop_words = result.words_no_stop_words
        self.words_all_filters = result.words_all_filters

        util.debug(20 * '*')
        util.debug('self.sentences in Keyword:\n', ' || '.join(self.sentences))
        util.debug('self.words_no_filter in Keyword:\n', self.words_no_filter)
        util.debug('self.words_no_stop_words in Keyword:\n', self.words_no_stop_words)
        util.debug('self.words_all_filters in Keyword:\n', self.words_all_filters)

        options = ['no_filter', 'no_stop_words', 'all_filters']

        if vertex_source in options:
            _vertex_source = result['words_' + vertex_source]
        else:
            _vertex_source = result['words_all_filters']

        if edge_source in options:
            _edge_source = result['words_' + edge_source]
        else:
            _edge_source = result['words_no_stop_words']

        self.keywords = util.sort_words(_vertex_source, _edge_source, window=window, pagerank_config=pagerank_config)

    #获取最重要的num个长度大雨等于最低长度的关键词，返回关键词列表
    def get_keywords(self, num=6, word_min_len=1):

        result = []
        count = 0
        for item in self.keywords:
            if count >= num:
                break
            if len(item.word) >= word_min_len:
                result.append(item)
                count += 1
        return result

    #获取keywords_num个关键词构造的可能出现的词语，要求这个短语在原文本中至少出现的次数，返回关键词短语列表
    def get_keyphrases(self, keywords_num=12, min_occur_num=2):

        keywords_set = set([item.word for item in self.get_keywords(num=keywords_num, word_min_len=1)])
        keyphrases = set()
        for sentence in self.words_no_filter:
            one = []
            for word in sentence:
                if word in keywords_set:
                    one.append(word)
                else:
                    if len(one) > 1:
                        keyphrases.add(''.join(one))
                    if len(one) == 0:
                        continue
                    else:
                        one = []
            if len(one) > 1:
                keyphrases.add(''.join(one))

        return [phrase for phrase in keyphrases
                if self.text.count(phrase) >= min_occur_num]


if __name__ == '__main__':
    pass