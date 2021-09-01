function solution(n) {
  var answer = 0
  var new_n = n.toString(3)

  for (let i = 0; i < new_n.length; i++) {
    answer += ((3 ** i) * new_n[i])
  }

  return answer
}

solution(45)