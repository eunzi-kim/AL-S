function solution(arr, divisor) {
  var answer = [];
  for (let x of arr) {
    if (x % divisor == 0) {
      answer.push(x)
    }
  }
  if (answer.length) {
    answer.sort((a, b) => a-b)
  }
  else {
    answer = [-1]
  }
  return answer;
}