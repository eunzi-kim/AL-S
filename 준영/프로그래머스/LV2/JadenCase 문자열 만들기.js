function solution(s) {
  var answer = ''
  var idx = 0
  for (const i of s) {
    if (i === ' ') {
      answer += i
      idx = 0
      continue
    }

    if (idx === 0) {
      answer += i.toUpperCase()
      idx += 1
    } else {
      answer += i.toLowerCase()
    }
  }
  return answer
}