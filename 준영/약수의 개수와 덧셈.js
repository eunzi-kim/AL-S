function solution(left, right) {
  var answer = 0
  for (let i = left; i <= right; i++) {
    var idx = 1
    var cnt = 0
    while (idx <= i) {
      if (i % idx === 0) {
        cnt += 1
      }
      idx += 1
    }

    if (cnt % 2 === 0) {
      answer += i
    } else {
      answer -= i
    }
  }
  
  return answer
}