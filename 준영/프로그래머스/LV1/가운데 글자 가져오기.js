function solution(s) {
  var answer = '';
  var n = s.length
  if (n % 2 === 0) {
    answer = s.slice(n/2-1, n/2+1) 
  } else {
    answer = s.slice(parseInt(n/2),parseInt(n/2)+1)
  }
  return answer;
}

