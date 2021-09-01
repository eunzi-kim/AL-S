function solution(progresses, speeds) {
  var answer = [];
  const n = progresses.length
  var day = []
  for (let i=0; i<n; i++) {
    var r = 100 - progresses[i]
    var d = 0
    while (r>0) {
      r -= speeds[i]
      d += 1
    } 
    day.push(d)
  }
  var i = 0
  var cnt = 1
  var pre = day[0]
  while (i<n) {
    if (i<n-1 && pre >= day[i+1]) {
      cnt += 1
      i += 1
    } else {
      answer.push(cnt)
      if (i<n-1) {
        pre = day[i+1]
      }
      cnt = 1
      i += 1
    }
  }
  return answer;
}

p = [93, 30, 55, 60, 40, 65]
s = [1, 30, 5 , 10, 60, 7]
console.log(solution(p, s))