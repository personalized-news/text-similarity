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
