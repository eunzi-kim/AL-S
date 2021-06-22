function solution(s) {
  var answer = '';
  var i = 0
  for (let x of s) {
    if (x === " ") {
      answer += x
      i = 0
    }
    else {
      if (i % 2 === 0) {
        answer += x.toUpperCase()
      } else {
        answer += x.toLowerCase()
      }
      i += 1
    }
  }
  return answer;
}