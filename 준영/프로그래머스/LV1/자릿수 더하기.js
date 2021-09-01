function solution(n) {
  var answer = 0
  for (const i of String(n)) {
    answer += parseInt(i)
  }
  return answer
}