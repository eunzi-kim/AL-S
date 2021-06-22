function solution(numbers) {
  var answer = [];
  for (let i=0; i<numbers.length; i++) {
    for (let j=i+1; j<numbers.length; j++) {
      var x = numbers[i] + numbers[j]
      if(!answer.includes(x)) {
        answer.push(x)
      }
    }
  }
  answer.sort((a, b) => a-b)
  return answer;
}

numbers = [5, 0, 2, 7]
console.log(solution(numbers))