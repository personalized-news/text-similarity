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
