function solution(s) {
  const n = s.length
  var answer = n
  for (let x=1; x<n; x++) {
    var exam = ''
    var pre = ''
    var cnt = 0
    for (let i=0; i<n; i+=x) {
      if (s.slice(i, i+x) !== pre) {
        if (cnt > 1) {
          exam += String(cnt) + pre
        } else {
          exam += pre
        }
        pre = s.slice(i, i+x)
        cnt = 1
        if (i >= n-x) {
          exam += pre
        }
      } else {
        if (i >= n-x) {
          exam += String(cnt+1) + s.slice(i, i+x)
        }
        cnt += 1
      }
    }
    if (answer > exam.length) {
      answer = exam.length
    }
  }
  return answer;
}

s = "abcabcdede"
console.log(solution(s))