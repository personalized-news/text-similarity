#coding:utf-8

import os
import re
import sys
#打开文件的时候要指定编码,否则写入的时候会乱码
output = open('context.txt', 'w', encoding="utf-8")

datepat = re.compile(r'[\!\%\[\]\,\。\？\?]')
with open('../corpus.txt', encoding='utf-8',  mode = 'r') as f:
    for line in f:
        line = line.strip("\n")
        line = datepat.sub("", line)
        output.write(line)
        output.write("\n")

# 关闭文件
f.close()
output.close()