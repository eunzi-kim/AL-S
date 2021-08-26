function solution(arr) {
  var answer = []
  answer.push(arr[0])
  var idx = 0
  for (const temp of arr) {
    if (answer[idx] != temp) {
      answer.push(temp)
      idx += 1
    }
  }
  return answer
}