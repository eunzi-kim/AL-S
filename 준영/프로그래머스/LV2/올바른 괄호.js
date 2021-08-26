function solution(s){
  var answer = true
  const stack = []
  for (const i of s) {
    if (i == '(') {
      stack.push('(')
    } else {
      if (stack.length > 0) {
        stack.pop()
      } else {
        answer = false
        break
      }
    }
  }
  if (stack.length > 0) {
    answer = false
  }
  return answer
}