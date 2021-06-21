function solution(n) {
  var answer = 0
  var arr = []
  for (const i of String(n)) {
    arr.push(i)
  }
  arr.sort((a, b) => b - a)
  answer = arr.join('')
  answer = parseInt(answer)
  return answer
}

solution(118372)