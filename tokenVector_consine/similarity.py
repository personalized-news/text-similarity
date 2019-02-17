 #!/usr/bin/env python3
# coding: utf-8
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import numpy as np
import jieba
from data import Data
from stopWord import getStopWord

d = Data()
class SimTokenVec:

    def __init__(self):
        # token_vector是单个词求向量的
        self.embedding_path = '../token_vector.bin'
        self.model = gensim.models.KeyedVectors.load_word2vec_format(self.embedding_path, binary=False)
    '''获取词向量文件'''
    def get_wordvector(self, word):#获取词向量
        try:
            return self.model[word]
        except:
            return np.zeros(200)

    '''基于余弦相似度计算句子之间的相似度，句子向量等于字符向量求平均'''
    def similarity_cosine(self, word_list1,word_list2):# 给予余弦相似度的相似度计算
        vector1 = np.zeros(200) # 返回具有输入形状和类型的零数组
        for word in word_list1:
            vector1 += self.get_wordvector(word) # 得到每个词的向量
        vector1=vector1/len(word_list1) # 句子向量为每个词向量求平均
        vector2=np.zeros(200)
        for word in word_list2:
            vector2 += self.get_wordvector(word)
        vector2=vector2/len(word_list2)

        cos1 = np.sum(vector1*vector2) # 向量乘积求和
        cos21 = np.sqrt(sum(vector1**2)) # 求向量长度
        cos22 = np.sqrt(sum(vector2**2))
        similarity = cos1/float(cos21*cos22)
        return  similarity

    '''去除停用词 '''
    def deleteStopWord(self, text):
        rightText = []
        stopWord = getStopWord()
        for str in text:
            if stopWord.count(str) == 0:
                rightText.append(str)
        return rightText

    '''计算句子相似度'''
    def distance(self, text1, text2):# 相似性计算主函数
        # 分词
        word_list1 = jieba.lcut(text1)
        word_list2 = jieba.lcut(text2)
        # 去除停用词
        word_list1 = self.deleteStopWord(word_list1)
        word_list2 = self.deleteStopWord(word_list2)
        # 合并成字符串
        word_list1 = ''.join(word_list1)
        word_list2 = ''.join(word_list2)
        # 转换为单个字符的列表
        word_list1 = list(word_list1)
        word_list2 = list(word_list2)
        return self.similarity_cosine(word_list1, word_list2)

simer = SimTokenVec()
def test():
    text1 = '我喜欢你'
    text2 = '我喜欢你'
    sim = simer.distance(text1, text2)
    print('测试：', sim)
test()

checkData = d.getCheckData()
question = d.getQuestion()
answer = d.getAnswer()
que = question.split('|')
ans = answer.split(',')
import datetime
import jieba.analyse
def get_accuracy():
    correct = 0
    str = ''
    min = 0
    disc = 0
    for i, qv in enumerate(que):
        min = 0
        for j, cv in  enumerate(checkData):
            disc = simer.distance(qv, cv)
            if disc >= min:
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
