
function solution(n) {
    var answer = 0
    var pre = []
    var n;
    while (n >= 3) {
        pre.push(n%3)
        n = Math.floor(n/3)
    }
    pre.push(n)
    console.log(pre)

    pre.reverse()
    for (let i=0; i<pre.length; i++) {
        answer += pre[i]*(Math.pow(3, i))
    }

    return answer
}

console.log(solution(45))