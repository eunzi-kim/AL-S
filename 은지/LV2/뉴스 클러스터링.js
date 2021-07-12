function solution(str1, str2) {
  var answer = 0;
  const s1 = str1.toUpperCase()
  const s2 = str2.toUpperCase()
  var a = []
  var b = []
  for (let i=0; i<s1.length-1; i++) {
    const s = s1.slice(i, i+2)
    if (s.match(/[A-Z]{2}/)) {
      a.push(s)
    }
  }
  for (let j=0; j<s2.length-1; j++) {
    const ss = s2.slice(j, j+2)
    if (ss.match(/[A-Z]{2}/)) {
      b.push(ss)
    }
  }
  
  var inter = 0
  a.sort()
  b.sort()
  var i = 0
  var j = 0
  while (i < a.length && j < b.length) {
    if (a[i] === b[j]) {
      inter += 1
      i += 1
      j += 1
    } else if (a[i] < b[j]) {
      i += 1
    } else {
      j += 1
    }
  }
  const union = a.length + b.length - inter
  
  if (union === 0) {
    answer = 65536
  } else {
    answer = parseInt((inter / union) * 65536)
  }
  return answer;
}

str1 = "handshake"
str2 = "shake hands"
console.log(solution(str1, str2))