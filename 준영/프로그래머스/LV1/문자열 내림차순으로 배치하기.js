function solution(s) {
  var answer = ''
  var arr = s.split('')
  arr.sort((a, b) => a < b ? 1 : a > b ? -1: 0)
  answer = arr.join("")
  return answer
}

console.log(solution("Zbcdefg"))
