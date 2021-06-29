function solution(s) {
  var answer = 0
  var stack = []
  for (let i = 0; i < s.length; i++) {
    if (stack.length === 0) {
      stack.push(s[i])
      continue
    }

    if (stack[stack.length-1] === s[i]) {
      stack.pop()
    } else {
      stack.push(s[i])
    }
  }

  if (stack.length === 0) {
    answer = 1
  }

  return answer
}