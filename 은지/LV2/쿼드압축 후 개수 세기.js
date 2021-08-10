var zero = 0
var one = 0

function search(r, c, n, arr) {
  var chk = 1
  for (let i=r; i<r+n; i++) {
    for (let j=c; j<c+n; j++) {
      if (arr[r][c] !== arr[i][j]) {
        chk = 0
        break
      }
    }
    if (chk === 0) {break}
  }
  if (chk === 1) {
    if (arr[r][c] === 1) {
      one += 1
    } else {
      zero += 1
    }
  }
  else {
    for (let k=r; k<r+n; k+=parseInt(n/2)) {
      for (let l=c; l<c+n; l+=parseInt(n/2)) {
        search(k, l, parseInt(n/2), arr)
      }
    }
  }
}


function solution(arr) {
  search(0, 0, arr.length, arr)
  var answer = [zero, one]
  return answer;
}