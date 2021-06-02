function solution(answers) {
  var answer = []
  const number_one = [1, 2, 3, 4, 5]
  const number_two = [1, 3, 4, 5]
  const number_three = [3, 1, 2, 4, 5]

  var one_idx = 0
  var two_idx = 0
  var three_idx = 0

  const numbers = Array.from({length: 3}, () => 0)
  
  for (const element of answers) {
    // 1번
    if (number_one[one_idx] === element) {
      numbers[0] += 1
    }
    one_idx += 1
    if (one_idx === 5) {
      one_idx = 0
    }

    // 2번
    if (two_idx % 2 === 0) {
      if (element === 2) {
        numbers[1] += 1
      }
    } else {
      if (number_two[parseInt(two_idx/2)] === element) {
        numbers[1] += 1
      }
    }

    two_idx += 1
    if (two_idx === 8) {
      two_idx = 0
    }

    // 3번
    if (number_three[parseInt(three_idx/2)] === element) {
      numbers[2] += 1
    }
    three_idx += 1
    if (three_idx === 10) {
      three_idx = 0
    }
    
  }

  var max_num = Math.max.apply(null, numbers)
  for (const item in numbers) {
    if (numbers[item] === max_num) {
      answer.push(Number(item)+1)
    }
  }

  return answer
}

var answer = [1,2,3,4,5]
console.log(solution(answer))
var answer = [1,3,2,4,2]
console.log(solution(answer))