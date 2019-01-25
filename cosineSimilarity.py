# coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import jieba
import numpy

from collections import Counter

def getCosineSimilarity(str1, str2):
    words = set() # 创建集合
    seg_list1 = jieba.lcut(str1) # 分词 返回list
    seg_list2 = jieba.lcut(str2)
    seg_list_number1 = Counter(seg_list1) # 计算list里的每个元素的出现次数
    seg_list_number2 = Counter(seg_list2)

    # 把分好的词装入集合，去重
    for value in seg_list1:
        words.add(value) # 把分好的词放入集合中，去重

    for value in seg_list2:
        words.add(value) # 把分好的词放入集合中，去重

    # 遍历集合，生成向量, 计算余弦值

    vector_product = 0
    vector_length_product1 = 0
    vector_length_product2 = 0
    for word in words:
        num1 = seg_list_number1[word]
        num2 = seg_list_number2[word]
        vector_product += num1 * num2
        vector_length_product1 += num1 * num1
        vector_length_product2 += num2 * num2
    return vector_product / numpy.sqrt(vector_length_product1 * vector_length_product2)
