function solution(N, stages) {
  var answer = []
  var arr = Array.from({length: N}, x => 0)
  for (const i of stages) {
    for (let j = 0; j < i-1; j++) {
      arr[j] += 1
    }
  }

  var fail = Array.from({length: N}, (x, i) => [0, i+1])

  var div = stages.length

  for (let i = 0; i < N; i++) {
    if (div === 0) {
      fail[i][0] = 0
    } else {
      fail[i][0] = (div - arr[i]) / div
    }
    div = arr[i]
  }
  
  fail.sort(function (a, b) {
    return b[0] - a[0]
  })

  answer = fail.map(x => x[1])
  return answer
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))