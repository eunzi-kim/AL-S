function solution(n) {
    var answer = 0;
    for (let x=1; x<=n; x++) {
      if (n % x === 0) {
        answer += x
      }
    }
    return answer;
}