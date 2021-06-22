function solution(n) {
  var answer = 0
  var temp = n ** 0.5
  if (Number.isInteger(temp)) {
    answer = (temp + 1) ** 2
  } else {
    answer = -1
  }
  return answer
}

solution(121)