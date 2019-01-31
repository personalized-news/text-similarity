#coding:utf-8
import jieba

output = open('words.txt', 'w', encoding="utf-8")

with open('context.txt', encoding='utf-8',  mode = 'r') as f:
    for line in f:
        seg_list = jieba.cut(line)
        output.write(" ".join(seg_list) + '\n')

f.close()
output.close()

