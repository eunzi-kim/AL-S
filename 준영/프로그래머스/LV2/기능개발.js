function solution(progresses, speeds) {
  var answer = []
  var n = progresses.length
  var arr = Array.from({length: n}, x => 0)
  for (let i = 0; i < n; i++) {
    if ((100 - progresses[i]) % speeds[i] === 0) {
      arr[i] = parseInt((100 - progresses[i])/speeds[i])
    } else {
      arr[i] = parseInt((100 - progresses[i])/speeds[i]) + 1
    }
  }
  var temp = arr[0]
  var result = 1
  for (let i = 1; i < n; i++) {
    if (temp < arr[i]) {
      answer.push(result)
      result = 1
      temp = arr[i]
    } else {
      result += 1
    }
  }
  answer.push(result)

  return answer
}