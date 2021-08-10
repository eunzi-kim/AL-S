function quard(arr, idx, visit, x, y) {
  var result = true
  var zero_one = arr[x][y]
  for (let i = x; i < x+idx; i++) {
    for (let j = y; j < y+idx; j++) {
     if (arr[i][j] != zero_one) {
       result = false
     } 
    }
  }
  
  if (result) {
    for (let i = x; i < x+idx; i++) {
      for (let j = y; j < y+idx; j++) {
        visit[i][j] = 1
      }
    }
    return zero_one
  } else {
    return -1
  }
  

}

function solution(arr) {
  var answer = [0, 0]
  var n = arr.length
  var visit = Array.from(Array(n), () => Array(n).fill(0))
  
  var idx = n

  while (idx >= 1) {
    for (let i = 0; i < n; i += idx) {
      for (let j = 0; j < n; j += idx) {
        if (visit[i][j] == 0) {
          var zo = quard(arr, idx, visit, i, j)
          if (zo != -1) answer[zo] += 1
        }
      }
    }
    idx = parseInt(idx/2)
  }
  return answer
}


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	
solution(arr)