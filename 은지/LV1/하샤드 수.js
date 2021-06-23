function solution(x) {
  var answer = true
  // 자릿수 합
  var y = x
  var v = 0
  while (y > 0) {
    v += y % 10
    y = parseInt(y / 10)
  }
  // 조건
  if (x % v) {
    answer = false
  }
  return answer
}