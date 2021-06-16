function solution(strings, n) {
  var answer = []
  strings.sort()
  strings.sort((a, b) => a[n] < b[n] ? -1 : a[n] > b[n] ? 1: 0)
  answer = strings
  return answer
}