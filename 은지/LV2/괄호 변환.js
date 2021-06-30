function division(w) {
  var l = 0
  var r = 0
  for (let i=0; i<w.length; i++) {
    if (w[i] === "(") {
      l += 1
    } else {
      r += 1
    }
    if (l === r) {
      return i
    }
  }
}


function chk(s) {
  var stack = []
  for (let i=0; i<s.length; i++) {
    if (s[i] === "(") {
      stack.push("(")
    } else {
      if (stack.length) {
        stack.pop()
      }
    }
  }
  return stack.length
}


function solution(p) {
  var answer = ''
  if (chk(p) === 0) {
    answer = p
  } else {
    var i = division(p)
    var u = p.slice(0, i+1)
    var v = p.slice(i+1, )
    if (chk(u) === 0) {
      return u + solution(v)
    } else {
      answer = '(' + solution(v) + ')'
      for (let i=1; i<u.length-1; i++) {
        if (u[i] === '(') {
          answer += ')'
        } else [
          answer += '('
        ]
      }
    }
  }
  return answer
}


p = "()))((()"
console.log(solution(p))