#!/usr/bin/env python3
# coding: utf-8
#正确匹配了 925 题
#正确率为： 0.7023538344722855
from time import time
import os
from gensim.models import KeyedVectors
from data import Data
from stopWord import getStopWord
import datetime
import jieba

# 初始化日志
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')

start = time()


if not os.path.exists('../sgns.financial.word'):
    raise ValueError("SKIP: sgns.financial.word 不存在")

model = KeyedVectors.load_word2vec_format('../model/token_vector.bin', binary=False)

print('Cell took %.2f seconds to run.' % (time() - start))

model.init_sims(replace=True)

# 获取数据
d = Data()
checkData = d.getCheckData()
question = d.getQuestion()
answer = d.getAnswer()
que = question.split('|')
ans = answer.split(',')
# 去除停用词
def deleteStopWord(text):
    rightText = []
    stopWord = getStopWord()
    for str in text:
        if stopWord.count(str) == 0:
            rightText.append(str)
    return rightText

def get_accuracy():
    correct = 0
    str = ''
    min = 0
    disc = 0
    for i, qv in enumerate(que):
        min = float('inf')
        sen1 = deleteStopWord(jieba.lcut(qv))
        sen1 = ''.join(sen1)
        for j, cv in  enumerate(checkData):
            sen2 = deleteStopWord(jieba.lcut(cv))
            sen2 = ''.join(sen2)
            disc = model.wmdistance(list(sen1), list(sen2))
            if disc <= min:
                min = disc
                str = cv
        if str == ans[i]:
            correct = correct + 1
    # simer.distance('我想问一下，外币证券转银证的金额有限制吗？', '我叫叶文俊')
    print ("正确匹配了" , correct , "题")
    print ("正确率为：" , correct / 1317.0)
    return

start_time = datetime.datetime.now()
get_accuracy()
end_time = datetime.datetime.now()

interval = (end_time - start_time).seconds
print ('need time: ', interval)




