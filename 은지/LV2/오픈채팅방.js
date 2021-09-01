function solution(record) {
  var answer = [];
  var info = {}
  for (let v of record) {
    const x = v.split(" ")
    if (x[0] !== 'Leave') {
      info[x[1]] = x[2]
    }
  }
  for (let w of record) {
    const y = w.split(" ")
    var message = ''
    if (y[0] === 'Enter') {
      message = info[y[1]] + "님이 들어왔습니다."
      answer.push(message)
    }
    else if (y[0] === 'Leave') {
      message = info[y[1]] + "님이 나갔습니다."
      answer.push(message)
    }
  }
  return answer;
}