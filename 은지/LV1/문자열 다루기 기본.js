function solution(s) {
  var answer = true;
  if (s.length !== 4 && s.length !== 6) {
    answer = false
  }
  for (let x of s) {
    if (isNaN(Number(x))) {
      answer = false
    }
  }
  return answer;
}