function solution(n) {
  var answer = []
  var total = 0
  const temp = []

  for (let i = 1; i <= n; i++) {
    temp.push(new Array(i).fill(0)) 
    total += i
  }
  
  let move = n
  let now = 0

  let i = -1
  let j = 0

  let direction = 0

  while (now < total) {
    direction %= 3

    if (direction === 0) {
      for (let t = 0; t < move; t++) {
        i += 1
        now += 1
        temp[i][j] = now
      }
    }
    if (direction === 1) {
      for (let t = 0; t < move; t++) {
        j += 1
        now += 1
        temp[i][j] = now
      }
    }
    if (direction === 2) {
      for (let t = 0; t < move; t++) {
        i -= 1
        j -= 1
        now += 1
        temp[i][j] = now
      }
    }

    move -= 1
    direction += 1

  }
  
  for (const tem of temp) {
    for (const k of tem) {
      answer.push(k)
    }
  }

  
  return answer
}
solution(4)