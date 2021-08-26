function balanced_index(p) {
  var count = 0
  for (let i = 0; i < p.length; i++) {
    if (p[i] === '(') {
      count += 1
    } else {
      count -= 1
    }
    if (count === 0) {
      return i
    }
  }
}

function check_proper(p) {
  var count = 0
  for (const i of p) {
    if (i === '(') {
      count += 1
    } else {
      if (count === 0) {
        return false
      }
      count -= 1
    }
  }
  return true
}

function solution(p) {
  var answer = ''
  if (p === '') return answer

  var index = balanced_index(p)
  var u = p.slice(0, index+1)
  var v = p.slice(index+1, p.length)
  
  if (check_proper(u)) {
    answer = u + solution(v)
  } else {
    answer = '('
    answer += solution(v)
    answer += ')'
    u = u.slice(1, u.length-1)
    var temp = Array.from({length: u.length}, x => 0)
    for (let i = 0; i < u.length; i++) {
      if (u[i] === '(') {
        temp[i] = ')'
      } else {
        temp[i] = '('
      }
    }
    answer += temp.join('')
  }

  return answer
}

console.log(solution("()))((()"))