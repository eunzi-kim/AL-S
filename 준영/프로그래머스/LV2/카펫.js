function solution(brown, yellow) {
  var answer = []
  var total = brown + yellow
  var idx = total
  while (idx > 0) {
    if (total % idx == 0) {
      var x = idx
      var y = total / idx
      if ((x + y) * 2 - 4 === brown) {
        answer.push(x)
        answer.push(y)
        break
      }
    }
    idx -= 1
  }
  return answer
}