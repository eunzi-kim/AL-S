function solution(n) {
  var r = []
  while (n>0) {
    if (n % 3 === 1) {
      r.push('1')
      n = parseInt(n/3)
    }
    else if (n % 3 === 2) {
      r.push('2')
      n = parseInt(n/3)
    }
    else {
      r.push('4')
      n = parseInt(n/3)-1
    }
  }
  r.reverse()
  const answer = r.join('')
  return answer;
}