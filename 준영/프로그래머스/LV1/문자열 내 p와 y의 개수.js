function solution(s){
  var answer = true;
  s = s.toLowerCase()
  var p_cnt = 0
  var y_cnt = 0
  for (const i of s) {
    if (i === 'p') {
      p_cnt += 1
    } 
    if (i === 'y') {
      y_cnt += 1
    } 
  }
  if (p_cnt === y_cnt) {
    answer = true
  } else {
    answer = false
  }
  return answer;
}