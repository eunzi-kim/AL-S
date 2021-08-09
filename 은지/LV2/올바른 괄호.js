function solution(s) {
  var stack = []
  for (let x of s) {
    if (stack.length === 0) {
      if (x === ")") {
        return false
      } else {
        stack.push(x)
      }
    }
    else {
      if (x === "(") {
        stack.push(x)
      } else {
        stack.pop()
      }
    }
  }
  if (stack.length) {
    return false
  }
  return true
}