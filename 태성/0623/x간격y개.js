function solution(x, n) {
    var answer = [];
    for (let i=1; i<n+1; i++) {
        answer.push(x*i)
    }
    return answer;
}