#!/usr/bin/env python3
# coding: utf-8
#正确匹配了 925 题
#正确率为： 0.7023538344722855
#need time:  1584

from time import time
import os
from gensim.models import KeyedVectors
import datetime
import jieba
from gensim.similarities import WmdSimilarity

from data import Data
from stopWord import getStopWord

# 初始化日志
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')

start = time()


if not os.path.exists('../model/token_vector.bin'):
    raise ValueError("SKIP: model/token_vector.bin 不存在")

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


# 去除checkData的停用词
wmd_corpus = []
for i, value in enumerate(checkData):
    val = ''.join(deleteStopWord(jieba.lcut(value)))
    wmd_corpus.append(list(val))


# 初始化 WmdSimilarityv
num_best = 1
instance = WmdSimilarity(wmd_corpus, model, num_best=1)


def get_accuracy():
    correct = 0
    for i, qv in enumerate(que):
        qvVaule = ''.join(deleteStopWord(jieba.lcut(qv)))
        sim = instance[list(qvVaule)]
        print(sim)
        if checkData[sim[0][0]] == ans[i]:
            correct = correct + 1
    print ("正确匹配了" , correct , "题")
    print ("正确率为：" , correct / 1317.0)
    return


start_time = datetime.datetime.now()
get_accuracy()
end_time = datetime.datetime.now()

interval = (end_time - start_time).seconds
print ('need time: ', interval)