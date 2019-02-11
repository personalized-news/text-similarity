'use strict';

const { answer, checkData, questions } = require('./data');

function lenvenshteinDistance(s, t) {
    const sLen = s.length;
    const tLen = t.length;
    let substitutionCost = 0;
    const d = [];
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

function findBest(event) {
    console.time('findBest')
    const len = checkData.length;
    const min = 100;
    let res;
    event.preventDefault();
    const input = document.querySelector('input');
    const span = document.querySelector('span');
    for(const i = 0; i < len; i ++) {
       const step = lenvenshteinDistance(input.value, checkData[i])
       if( step <= min){
           min = step;
           res = checkData[i];
       }
    }
    span.innerHTML = res + '<br>LenvenshteinDistance: ' + min;
    console.timeEnd('findBest')
}

/**
 * 测试LenvenshteinDistance的匹配准确度
 * return 准确度 %
 * */

function getAccuracy() {
    // const span = document.querySelectorAll('span')[1];
    // console.log(questions.replace(/\n/g, "|"))
    const que = questions.split('\n');
    const ans = answer.split('\n');
    const total = que.length, queLen = que.length;
    let correct = 0;
    let min, matchStr;
    const checkDataLen = checkData.length;
    for(let i = 0; i < queLen; i ++) {
        min = 1000;
        for(let j = 0; j < checkDataLen; j ++) {
            const step = lenvenshteinDistance(que[i], checkData[j])
            if(step <= min) {
                min = step
                matchStr = checkData[j];
            }
        }
        if(matchStr === ans[i]) {
            correct++;
        }
    }
    console.log(`共有${que.length}几个问题,有${ans.length}个标准问\n` + `正确匹配了${correct}个问题 ` + '匹配正确率为：' + correct / total);
}

getAccuracy();
