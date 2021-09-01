function solution(arr) {
  const sum_v = arr.reduce((a, b) => a+b)
  var answer = sum_v / arr.length
  return answer;
}