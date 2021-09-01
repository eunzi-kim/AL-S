function solution(m, n, board) {
  var b = []
  for (let r=0; r<m; r++) {
    var sub_b = []
    for (let c=0; c<n; c++) {
      sub_b.push(board[r][c])
    }
    b.push(sub_b)
  }

  var dr = [0, 1, 0, 1]
  var dc = [0, 0, 1, 1]
  var answer = 0;

  while (true) {
    var chk = new Array(m)
    for (let mm=0; mm<m; mm++) {
      chk[mm] = new Array(n)
      for (let nn=0; nn<n; nn++) {
        chk[mm][nn] = 0
      }
    }
    var cnt = 0
    for (let r=0; r<m-1; r++) {
      for (let c=0; c<n-1; c++) {
        var friends = b[r][c]
        if (friends !== "0") {
          var ccnt = 0
          for (let i=1; i<=3; i++) {
            ccnt += 1
            if (b[r+dr[i]][c+dc[i]] !== friends) {
              break
            }
            if (ccnt === 3) {
              cnt += 1
              for (let j=0; j<4; j++) {
                chk[r+dr[j]][c+dc[j]] = 1
              }
            }
          }
        }
      }
    }
  
    if (cnt === 0) {
      break
    }

    for (let r=0; r<m; r++) {
      for (let c=0; c<n; c++) {
        if (chk[r][c] === 1) {
          answer += 1
          for (let k=r-1; k>=0; k--) {
            b[k+1][c] = b[k][c]
          }
          b[0][c] = "0"
        }
      }
    }
  }

  return answer;
}

m = 5
n = 6
b = ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]
console.log(solution(m, n, b))