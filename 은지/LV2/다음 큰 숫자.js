function count(s) {
  var cnt = 0
  for (let v of s) {
    if (v === "1") {
      cnt += 1
    }
  }
  return cnt
}

function solution(n) {
  var answer = 0;
  var m = count(n.toString(2))  
  for (let x=n+1; x<1000001; x++) {
    if (count(x.toString(2)) === m) {
      answer = x
      break
    }
  }
  return answer;
}