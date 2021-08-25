function solution(n) {
  var answer = 0;
  for (let x=1; x<=n; x++) {
    var sub_a = 0
    var y = x
    while (sub_a < n) {
      sub_a += y
      y += 1
      if (sub_a === n) {
        answer += 1
      }
    }
  }
  return answer;
}