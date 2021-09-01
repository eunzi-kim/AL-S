function solution(strings, n) {
    var answer = [];
    
    var pre = []
    for (let s of strings) {
        pre.push([s[n], s])
    }
    // console.log(pre)
    pre.sort()
    // console.log(pre)
    for (let p of pre) {
        answer.push(p[1])
    }
    return answer;
}