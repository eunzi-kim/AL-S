function solution(numbers) {
  var answer = []
  for (var n of numbers) {
    const temp = []
    while (n) {
      temp.push(n % 2)
      n = parseInt(n / 2)
    }
    temp.push(0)
    
    for (let i = 0; i < temp.length; i++) {
      if (i === 0 && temp[i] === 0) {
        temp[i] = 1
        break
      }

      if (temp[i] === 0) {
        temp[i-1] = 0
        temp[i] = 1
        break
      }
    }
    t = 0
    s = 1

    for (const i of temp) {
      t += i * s
      s *= 2
    }

    answer.push(t)
  }
  return answer
}

numbers = [2, 7]
solution(numbers)