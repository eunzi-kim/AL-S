function solution(places) {
  var answer = [];
  for (let p of places) {
    var person = []
    for (let i=0; i<5; i++) {
      for (let j=0; j<5; j++) {
        if (p[i][j] === "P") {
          person.push([i, j])
        }
      }
    } 
    var cnt = 1
    while (person.length) {
      const v = person.shift()

      function chk(r, c) {
        // 1칸 확인
        if (r+1 < 5 && p[r+1][c] === "P") {
          return 0
        }
        if (c+1 < 5 && p[r][c+1] === "P") {
          return 0
        }
        // 2칸 확인
        if (r+2 < 5 && p[r+2][c] === "P" && p[r+1][c] !== "X") {
          return 0
        }
        if (c+2 < 5 && p[r][c+2] === "P" && p[r][c+1] !== "X") {
          return 0
        }
        // 대각선 확인
        if (0 <= r-1 && c+1 < 5 && p[r-1][c+1] === "P") {
          if (p[r-1][c] !== "X" || p[r][c+1] !== "X") {
            return 0
          }
        }
        if (r+1 < 5 && c+1 < 5 && p[r+1][c+1] === "P") {
          if (p[r+1][c] !== "X" || p[r][c+1] !== "X") {
            return 0
          }
        }
      }

      var chk_v = chk(v[0], v[1])
      
      if (chk_v == 0) {
        cnt = 0
        break
      }
    }
    if (cnt) {
      answer.push(1)
    } else {
      answer.push(0)
    }
  }
  return answer;
}