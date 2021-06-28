function solution(num) {
  var answer = 0
  while (num != 1) {
    if (answer >= 500) {
      break
    }

    if (num % 2) {
      num = (num * 3) + 1
    } else {
      num = parseInt(num / 2)
    }

    answer += 1
  }

  if (num != 1) {
    answer = -1
  }
  return answer
}