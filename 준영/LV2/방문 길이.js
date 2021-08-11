function solution(dirs) {
  var answer = 0
  const dict = []
  var now = [0, 0]

  for (let i = 0; i < dirs.length; i++) {
    const t = dirs[i];
    var temp1 = [...now]
    if (t === 'U') {
      now[1] += 1
      if (now[1] > 5) {
        now[1] -= 1
        continue
      }
    } else if(t === 'D'){
      now[1] -= 1
      if (now[1] < -5) {
        now[1] += 1
        continue
      }
    } else if(t === 'L'){
      now[0] -= 1
      if (now[0] < -5) {
        now[0] += 1
        continue
      }
    } else if(t === 'R'){
      now[0] += 1
      if (now[0] > 5) {
        now[0] -= 1
        continue
      }
    }
    var temp2 = [...now]
    var path1 = String(temp1) + String(temp2)
    var path2 = String(temp2) + String(temp1)

    if (!dict.includes(path1)&&!dict.includes(path2)) {
      dict.push(path1)
      dict.push(path2)
      answer += 1
    }

  }

  return answer
}

dirs = 'ULURRDLLU'
solution(dirs)