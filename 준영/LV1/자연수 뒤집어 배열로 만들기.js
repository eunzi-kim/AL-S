function solution(n) {
  var answer = []
  var temp = String(n)
  for (let i = temp.length-1; i >= 0; i--) {
    answer.push(parseInt(temp[i]))
  }
  return answer
}
