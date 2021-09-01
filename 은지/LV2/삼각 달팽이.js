function solution(n) {
  var answer = [];
  var lst = new Array(n)
  for (let i=0; i<n; i++) {
    lst[i] = []
  }
  var max_x = 0
  for (let y=1; y<=n; y++) {
    max_x += y
  }
  var x = 1
  var c = 0
  var d = "-"
  var chk = new Array(n+1)
  for (let i=0; i<=n; i++) {
    chk[i] = 0
  }

  while (x<=max_x) {
    if (lst[c].length < c+1 && chk[c] === 0) {
      lst[c].push([x, d])
      x += 1
    }
    if (c+1<n && chk[c+1] === 0 && d === "+") {
      c += 1
    }
    else if (chk[c-1] === 0 && d === "-") {
      c -= 1
    }
    if (lst[c].length === c+1) {
      chk[c] = 1
      if (d === "+") {
        d = "-"
      }
      else {
        d = "+"
      }
    }
  }

  for (let i=0; i<n; i++) {
    for (let j=0; j<=i; j++) {
      if (lst[i][j][1] === "+") {
        answer.push(lst[i][j][0])
      }
    }
    for (let j=i; j>=0; j--) {
      if (lst[i][j][1] === "-") {
        answer.push(lst[i][j][0])
      }
    }
  }

  return answer;
}

n = 5
console.log(solution(n))