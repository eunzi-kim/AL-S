function solution(numbers) {
  var answer = '';
  var num = []
  for (let x of numbers) {
    num.push(String(x).repeat(3))
  }
  num.sort().reverse()
  for (let x of num) {
    answer += x.slice(0, parseInt(x.length/3))
  }
  if (answer[0] === '0') {
    answer = '0'
  }
  return answer;
}

numbers = [0, 0, 0]
console.log(solution(numbers))