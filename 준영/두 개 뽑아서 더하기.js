function solution(numbers) {
  var answer = []

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i; j < numbers.length; j++) {
      if (i != j) {
        var temp = numbers[i] + numbers[j]
        if (!answer.includes(temp)) {
          answer.push(temp)
        }
      }
    } 
  }

  answer.sort(function(a, b) {
    return a - b
  })
  return answer
}

solution([2,1,3,4,1])