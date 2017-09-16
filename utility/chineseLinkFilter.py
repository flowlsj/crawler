#! /usr/bin/env python
# --*-- coding:utf-8 --*--

import os
import sys
import re

if __name__=='__main__':
    if len(sys.argv) != 2:
        print """
            usage: python chineseLineFilter.py <file_to_be_filter>
        """
    input_path = sys.argv[1]
    origin_name = os.path.basename(input_path)
    origin_name = origin_name[0: origin_name.rfind('.')]
    output_path = input_path[0: input_path.rfind(os.sep) + 1] + origin_name + "_new.txt"

    chinese_pattern = re.compile(ur'^Title: [\u4E00-\u9FA5]+')

    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')

    line = input_file.readline()
    while line:
        if chinese_pattern.match(line.decode('utf-8')):
            output_file.write(line)
        line = input_file.readline()

    input_file.close()
    output_file.close()
