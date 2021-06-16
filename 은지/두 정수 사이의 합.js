function solution(a, b) {
  var answer = 0;
  var max_v = Math.max(a, b)
  var min_v = Math.min(a, b)
  for (let x=min_v; x<=max_v; x++) {
    answer += x
  }
  return answer;
}