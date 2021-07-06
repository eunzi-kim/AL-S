function solution(maps) {
  var answer = -1
  const n = maps.length
  const m = maps[0].length
  var check = new Array(n)
  for (let i=0; i<n; i++) {
    check[i] = new Array(m)
    for (let j=0; j<m; j++) {
      check[i][j] = 0
    }
  }
  var queue = [[0, 0]]
  check[0][0] = 1
  var dr = [-1, 1, 0, 0]
  var dc = [0, 0, -1, 1]

  while (queue.length > 0) {
    var v = queue.shift()
    var r = v[0]
    var c = v[1]
    for (let i=0; i<4; i++) {
      var new_r = r + dr[i]
      var new_c = c + dc[i]

      if (0 <= new_r && new_r < n && 0 <= new_c && new_c < m) {
        if (maps[new_r][new_c] === 1 && check[new_r][new_c] === 0) {
          queue.push([new_r, new_c])
          check[new_r][new_c] = check[r][c] + 1
        }        
      }
    }
  }

  if (check[n-1][m-1]) {
    answer = check[n-1][m-1]
  }
  return answer;
}

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
console.log(solution(maps))