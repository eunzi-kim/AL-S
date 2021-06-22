function solution(n) {
  var answer = [];
  for (let x=n; x>0; x=x) {
    answer.push(x % 10)
    x = parseInt(x / 10)
  }
  return answer;
}