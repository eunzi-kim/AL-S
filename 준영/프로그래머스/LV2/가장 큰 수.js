function solution(numbers) {
  var answer = ''
  var temp_numbers = numbers.map(x => String(x))
  temp_numbers.sort((a, b) => {
    var temp_a = String(a) + String(a) + String(a)
    var temp_b = String(b) + String(b) + String(b)
    if (temp_a > temp_b) {
      return -1
    }
    if (temp_a < temp_b) {
      return 1
    }
    return 0
  })
  answer = temp_numbers.join('')
  if (Number(answer) === 0) return '0'
  return answer
}


console.log(solution([6, 10, 2]))
console.log(solution([3, 30, 34, 5, 9]))