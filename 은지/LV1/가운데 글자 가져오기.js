function solution(s) {
  var answer = '';
  // 단어의 길이가 홀수
  if (s.length % 2) {
    answer = s[parseInt(s.length/2)]
  }
  // 단어의 길이가 짝수
  else {
    answer = s[parseInt(s.length/2)-1] + s[parseInt(s.length/2)]
  }
  return answer;
}