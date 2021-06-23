function solution(phone_number) {
  var answer = '';
  const n = phone_number.length
  for (let i=0; i<n; i++) {
    if (i < n-4) {
      answer += "*"
    }
    else {
      answer += phone_number[i]
    }
  }
  return answer;
}