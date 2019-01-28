# Text similarity algorithm
## Levenshtein distance javaScript version
```js
function lenvenshteinDistance(s, t) {
    let sLen = s.length;
    let tLen = t.length;
    let substitutionCost = 0;
    let d = [];
    // 初始化
    d[0] = [];
    for(let i = 0; i <= tLen; i ++) d[0][i] = i;
    // 打表
    for(let i = 1; i <= sLen; i ++) {
        d[i] = [i];
        for(let j = 1; j <= tLen; j ++) {
            if(s[i - 1] === t[j - 1]) {
                substitutionCost = 0;
            }else substitutionCost = 1;
            d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + substitutionCost)
        }
    }
    return d[sLen][tLen];
}
```
   ### After this method is tested by data, the result is:
   #### There are 1317 questions and 1317 standards.
   #### Correctly matched 541 questions.
   #### Matching accuracy was: 0.41078208048595294
## Cosine similarity python version
```python
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
```
   #### Correctly matched 730 questions.
   #### Matching accuracy was: 0.554290053151

## SimHash
```python
    class SimHaming:
    '''利用64位数，计算海明距离'''
    def haming_distance(self, code_s1, code_s2):
        x = (code_s1 ^ code_s2) & ((1 << 64) - 1)
        ans = 0
        while x:
            ans += 1
            x &= x - 1
        return ans
    '''利用相似度计算方式,计算全文编码相似度'''
    def get_similarity(self, a, b):
        if a > b :
            return b / a
        else:
            return a / b

    '''对全文进行分词,提取全文特征,使用词性将虚词等无关字符去重'''
    def get_features(self, string):
        word_list=[word.word for word in pseg.cut(string) if word.flag[0] not in ['u','x','w','o','p','c','m','q']]
        return word_list

    '''计算两个全文编码的距离'''
    def get_distance(self, code_s1, code_s2):
        return self.haming_distance(code_s1, code_s2)

    '''对全文进行编码'''
    def get_code(self, string):
        return Simhash(self.get_features(string)).value

    '''计算s1与s2之间的距离'''
    def distance(self, s1, s2):
        code_s1 = self.get_code(s1)
        code_s2 = self.get_code(s2)
        similarity = (100 - self.haming_distance(code_s1,code_s2)*100/64)/100
        return similarity

 ```
 #### Correctly matched 710 questions
 #### The correct rate is: 0.5391040242976461
 ## tokenVector 
 ```python
 class SimTokenVec:

    def __init__(self):
        self.embedding_path = './model/token_vector.bin'
        self.model = gensim.models.KeyedVectors.load_word2vec_format(self.embedding_path, binary=False)
        #self.model = word2vec.load('./model/token_vector.bin')
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

    '''计算句子相似度'''
    def distance(self, text1, text2):# 相似性计算主函数
        word_list1=[word for word in text1]
        word_list2=[word for word in text2]
        return self.similarity_cosine(word_list1,word_list2)
 ```
 #### Correctly matched 900 questions
 #### The correct rate is: 0.683371298405467
## Vector space model
```python
class SimVsm:

    '''比较相似度'''
    def distance(self, text1, text2):
        words1 = [word.word for word in pesg.cut(text1) if word.flag[0] not in ['u', 'x', 'w']]
        words2 = [word.word for word in pesg.cut(text2) if word.flag[0] not in ['u', 'x', 'w']]
        tfidf_reps = self.tfidf_rep([words1, words2])
        return self.cosine_sim(np.array(tfidf_reps[0]), np.array(tfidf_reps[1]))
    '''对句子进行tfidf向量表示'''
    def tfidf_rep(self, sents):
        sent_list = []
        df_dict = {}
        tfidf_list = []
        for sent in sents:
            tmp = {}
            for word in sent:
                if word not in tmp:
                    tmp[word] = 1
                else:
                    tmp[word] += 1
            tmp = {word:word_count/sum(tmp.values()) for word, word_count in tmp.items()}
            for word in set(sent):
                if word not in df_dict:
                    df_dict[word] = 1
                else:
                    df_dict[word] += 1
            sent_list.append(tmp)
        df_dict = {word :math.log(len(sents)/df+1) for word, df in df_dict.items()}
        words = list(df_dict.keys())
        for sent in sent_list:
            tmp = []
            for word in words:
                tmp.append(sent.get(word, 0))
            tfidf_list.append(tmp)
        return tfidf_list

    '''余弦相似度计算相似度'''
    def cosine_sim(self, vector1, vector2):
        cos1 = np.sum(vector1 * vector2)
        cos21 = np.sqrt(sum(vector1 ** 2))
        cos22 = np.sqrt(sum(vector2 ** 2))
        similarity = cos1 / float(cos21 * cos22)
        return similarity
```
