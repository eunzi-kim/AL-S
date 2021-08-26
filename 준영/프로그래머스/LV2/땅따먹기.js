function solution(land) {
  var answer = 0
  
  const N = land.length

  const d_arr = Array.from(Array(N), () => Array(4).fill(0))
  
  for (let i = 0; i < 4; i++) {
    d_arr[0][i] = land[0][i]
  }

  for (let i = 1; i < N; i++) {
    for (let j = 0; j < 4; j++) {
      var max_temp = 0
      for (let k = 0; k < 4; k++) {
        if (j === k) continue

        if (max_temp < d_arr[i-1][k]) {
          max_temp = d_arr[i-1][k]
        }
        d_arr[i][j] = land[i][j] + max_temp
      }
    }
  }

  for (let i = 0; i < 4; i++) {
    if (d_arr[N-1][i] > answer) {
      answer = d_arr[N-1][i]
    }
  }
  
  return answer
}

land = [[1,1,1,1],[2,2,2,3],[3,3,3,6],[4,4,4,7]]
solution(land)