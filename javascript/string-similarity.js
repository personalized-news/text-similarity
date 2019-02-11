'use strict';

const stringSimilarity = require('string-similarity');
const { answer, checkData, questions } = require('./data');

function getAccuracy() {
  const checkDataLen = checkData.length;
  const total = questions.length, queLen = questions.length;
  let correct = 0;

  for (let i = 0; i < queLen; i++) {
    let max = 0, matchStr;
    for (let j = 0; j < checkDataLen; j++) {
      const degree = stringSimilarity.compareTwoStrings(questions[i], checkData[j]);
      if (degree >= max) {
        max = degree;
        matchStr = checkData[j];
      }
    }
    if (matchStr === answer[i]) {
      correct++;
    }
  }
  console.log(`共有${questions.length}个问题,有${answer.length}个标准问\n正确匹配了${correct}个问题; 匹配正确率为: ${correct / total}`);
}

getAccuracy();
