function solution(n) {
  var answer = 0
  for (let i = 1; i < n+1; i++) {
    var temp = i
    var sum_a = i
    while (sum_a < n) {
      temp += 1
      sum_a += temp
    }
    if (sum_a === n) {
      answer += 1
    }
    
  }
  return answer
}