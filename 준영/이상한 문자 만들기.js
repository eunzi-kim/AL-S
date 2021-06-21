function solution(s) {
  var answer = ''
  var idx = 0
  for (const i of s) {
    if (i === " ") {
      answer += " "
      idx = 0
    } else {
      if (idx % 2 === 0) {
        answer += i.toUpperCase()
      } else {
        answer += i.toLowerCase()
      }
      idx += 1
    }
  }
  return answer
}