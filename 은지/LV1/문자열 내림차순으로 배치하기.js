function solution(s) {
  var answer = '';
  var arr = []
  for (let x of s) {
    arr.push(x)
  }
  arr.sort().reverse()
  answer = arr.join("")
  return answer;
}