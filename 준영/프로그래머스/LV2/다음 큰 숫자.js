function solution(n) {
  var answer = 0
  var result = []
  var temp = n

  while (temp) {
    result.push(temp%2)
    temp = parseInt(temp/2)
  }

  const cnt = result.filter((x) => x === 1).length

  var idx = 0
  while (true) {
    idx += 1
    var arr = Array(0)
    temp = n + idx
    while (temp) {
      arr.push(temp%2)
      temp = parseInt(temp/2)
    }

    if (cnt === arr.filter((x) => x === 1).length) {
      answer = n + idx
      break
    }

  }
  return answer
}

solution(78)