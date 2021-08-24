function solution(n) {
  var a = 0
  var b = 1
  for (let i=0; i<n-1; i++) {
    var c = a+b
    a = b % 1234567
    b = c % 1234567
  }
  var answer = b
  return answer;
}