function solution(brown, yellow) {
  var s = brown + yellow
  for (let x=s; x>=1; x--) {
    if (s % x === 0 && (x-2) * (parseInt(s/x)-2) === yellow) {
      var answer = [x, parseInt(s/x)]
      break
    }
  }
  return answer;
}