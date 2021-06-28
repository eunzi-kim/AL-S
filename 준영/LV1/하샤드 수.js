function solution(x) {
  var answer = false
  var temp = x
  var sum = 0
  while (temp) {
    sum += (temp % 10)
    temp = parseInt(temp / 10)
  }
  if (x % sum === 0) {
    answer = true
  }
  return answer
}