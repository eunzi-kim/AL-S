function solution(arr) {
  var answer = []
  var x = Math.min(...arr)
  var idx = arr.indexOf(x)
  arr.splice(idx, 1)
  answer = arr
  if (answer.length === 0) {
    answer = [-1]
  } 
  return answer
}