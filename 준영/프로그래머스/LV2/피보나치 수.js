function solution(n) {
  var answer = 0
  var x = 0
  var y = 1
  for (let i = 0; i < n-1; i++) {
    var temp = x + y
    x = y % 1234567
    y = temp % 1234567
  }
  answer = y
  return answer
}