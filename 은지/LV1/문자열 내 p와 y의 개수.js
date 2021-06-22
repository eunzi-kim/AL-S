function solution(s){
  var cnt_p = 0
  var cnt_y = 0
  for (let x of s) {
    if (x === 'p' || x === 'P') {
      cnt_p += 1
    }
    else if (x == 'y' || x === 'Y') {
      cnt_y += 1
    }
  }
  if (cnt_p === cnt_y) {
    var answer = true
  }
  else {
    var answer = false
  }

  return answer;
}