function solution(s) {
  var answer = 0
  if (s[0] === '-') {
    answer = parseInt(s.slice(1))
    answer *= -1
  } else {
    answer = parseInt(s)
  }
  return answer
}