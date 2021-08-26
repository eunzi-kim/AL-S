function solution(s) {
  var answer = 0
  var temp = s
  for (let i = 0; i < s.length; i++) {
    const my_stack = []
    var is_right = true
    for (const j of temp) {
      if (j === '[' || j === '{' || j === '(') {
        my_stack.push(j)
      } else if (my_stack.length === 0) {
        is_right = false
        break
      }

      if (j == ']') {
        if (my_stack[my_stack.length-1] === '[') {
          my_stack.pop()
        } else {
          is_right = false
          break
        }
      }

      if (j == '}') {
        if (my_stack[my_stack.length-1] === '{') {
          my_stack.pop()
        } else {
          is_right = false
          break
        }
      }

      if (j == ')') {
        if (my_stack[my_stack.length-1] === '(') {
          my_stack.pop()
        } else {
          is_right = false
          break
        }
      }
    }
    if (my_stack.length !== 0) {
      is_right = false
    }

    if (is_right) {
      answer += 1
    }
    var x = temp[0]
    temp = temp.substring(1) + x
  }
  return answer
}