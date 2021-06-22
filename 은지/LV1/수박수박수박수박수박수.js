function solution(n) {
  var answer = '';
  const example = '수박'
  for (let x=0; x<n; x++) {
    answer += example[x%2]
  }
  return answer;
}