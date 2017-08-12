#! /usr/bin/env python
# --*-- coding:utf-8 --*--

import sys
import codecs
import re

class FileParser(object):
    def __init__(self, file):
        self.file = file

    def parse(self, separator=u'-'):
        """
        Parse file to get word - meaning pairs
        :param separator: the separator between word and meaning
        :return: list of dict, key is word and value is meaning
        """
        word_list = []
        file = codecs.open(self.file, 'r', encoding='utf-8')
        lines = file.readlines()
        for line in lines:
            key_value = line.split(separator)
            if len(key_value) == 2:
                if key_value[1].endswith(u"\r\n"):
                    key_value[1] = key_value[1][:-2]
                word_dic = {"name": key_value[0], "meaning": key_value[1]}
                word_list.append(word_dic)

        return word_list

        # print file.readlines()

if __name__=="__main__":
    file_parser = FileParser(sys.argv[1])
    file_parser.parse(u"-")
