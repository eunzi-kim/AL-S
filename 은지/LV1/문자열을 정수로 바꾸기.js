function solution(s) {
  var answer = 0;
  // 음수
  if (s[0] === '-') {
    answer = Number(s.slice(1,)) * (-1)
  }
  // 양수
  else {
    answer = Number(s)
  }
  return answer;
}