function solution(s, n) {
  var answer = ''
  
  for (const i of s) {
    if (i === ' ') {
      answer += ' '
      continue
    }

    var x = i.charCodeAt()

    if (x >= 97 && x <= 122) {
      var to_charCode = (x - 'a'.charCodeAt() + n) % 26
      to_charCode += 'a'.charCodeAt()
      answer += String.fromCharCode(to_charCode)
    }
    
    if (x >= 65 && x <= 90) {
      var to_charCode = (x - 'A'.charCodeAt() + n) % 26
      to_charCode += 'A'.charCodeAt()
      answer += String.fromCharCode(to_charCode)
    }

  }

  return answer
}

solution('Z', 1)