const n = 12345

function solution(n) {
    var answer = [];
    var s_n = n.toString()
    for (let i=s_n.length-1; i>-1; i--) {
        answer.push(parseInt(s_n[i]))
    }
    return answer;
}

console.log(solution(n))