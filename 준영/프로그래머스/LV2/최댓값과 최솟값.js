function solution(s) {
  var answer = ''
  const arr = s.split(' ').map(Number)
  answer = String(Math.min(...arr)) + ' ' + String(Math.max(...arr))
  
  return answer
}