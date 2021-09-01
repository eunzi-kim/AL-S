function is_numeric(str){
  return /^\d+$/.test(str);
}

function solution(s) {
  var answer = false
  if (s.length === 4 || s.length === 6) {
    if (is_numeric(s)) {
      answer = true
    }
  }
  return answer
}