function is_partition(arr, x, y) {
  var dx = [-1, 1, 0, 0]
  var dy = [0, 0, 1, -1]

  var ddx = [-2, 2, 0, 0]
  var ddy = [0, 0, 2, -2]

  for (let i = 0; i < 4; i++) {
    var vx = x + dx[i]
    var vy = y + dy[i]
    
    var vvx = x + ddx[i]
    var vvy = y + ddy[i]

    if (vx < 0 || vy < 0 || vx >= 5 || vy >= 5) continue

    if (arr[vx][vy] === 'P') return false

    if (vvx < 0 || vvy < 0 || vvx >= 5 || vvy >= 5) continue

    if (arr[vvx][vvy] === 'P' && arr[vx][vy] !== 'X' ) return false

  }

  var dddx = [-1, -1, 1, 1]
  var dddy = [-1, 1, -1, 1]

  var dz = [[0, 3], [0, 2], [1, 3], [1, 2]]

  for (let i = 0; i < 4; i++) {
    var vx = x + dddx[i]
    var vy = y + dddy[i]
    
    if (vx < 0 || vy < 0 || vx >= 5 || vy >= 5) continue

    if (arr[vx][vy] === 'P') {
      var dz1 = dz[i][0]
      var dz2 = dz[i][1]

      var vvx = x + dx[dz1]
      var vvy = y + dy[dz1]

      var vvvx = x + dx[dz2]
      var vvvy = y + dy[dz2]

      if (arr[vvx][vvy] !== 'X' || arr[vvvx][vvvy] !=='X') return false
    }
  }

  return true
}

function solution(places) {
  var answer = []

  for (const place of places) {
    var temp = []
    for (const p of place) {
      temp.push(p.split(""))
    }
    
    var is_space = true

    for (let i = 0; i < 5; i++) {
      if (is_space) {
        for (let j = 0; j < 5; j++) {
          if (temp[i][j] === 'P') {
            if (!is_partition(temp, i, j)) {
              is_space = false
              break
            }
          }
        }
      }
    }

    if (is_space) answer.push(1)
    else answer.push(0)
  }
  return answer
}

var places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)