function solution(a, b) {
  var answer = 0
  if (a > b) {
    var temp = a
    a = b
    b = temp
  }
  for (let i = a; i <= b; i++) {
    answer += i
  }
  return answer
}