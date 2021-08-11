function solution(dirs) {
  var answer = 0;
  var record = []
  var now = [0, 0]
  for (let dir of dirs) {
    var r = now[0]
    var c = now[1]
    if (dir === "U") {
      r = now[0] + 1
    } else if (dir == "D") {
      r = now[0] - 1
    } else if (dir == "R") {
      c = now[1] + 1
    } else {
      c = now[1] - 1
    }

    if (-5 <= r && r <= 5 && -5 <= c && c <= 5) {
      var arr = ""
      if (now[0] < r) {
        arr = String(now[0]) + String(now[1]) + String(r) + String(c)
      } else if (now[0] > r) {
        arr = String(r) + String(c) + String(now[0]) + String(now[1])
      } else if (now[1] < c) {
        arr = String(now[0]) + String(now[1]) + String(r) + String(c)
      } else {
        arr = String(r) + String(c) + String(now[0]) + String(now[1])
      }      
      now = [r, c]
      record.push(arr)
    }
  }

  record.sort()
  var past = []
  for (let v of record) {
    if (past !== v) {
      answer += 1
      past = v
    }
  }
  return answer;
}

dirs = "ULURRDLLU"
console.log(solution(dirs))