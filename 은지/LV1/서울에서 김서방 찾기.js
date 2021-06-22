function solution(seoul) {
  var answer = '';
  for (let i=0; i<seoul.length; i++) {
    if (seoul[i] === 'Kim') {
      answer += '김서방은 ' + String(i) + '에 있다'
    }
  }
  return answer;
}