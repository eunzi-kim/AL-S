function solution(arr, divisor) {
  var answer = []
  for (const temp of arr) {
    if (temp % divisor === 0) {
      answer.push(temp)
    }
  }
  answer.sort((a,b) => a-b)
  if (answer.length === 0) {
    answer.push(-1)
  }
  return answer
}