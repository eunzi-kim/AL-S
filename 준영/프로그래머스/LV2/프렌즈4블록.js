function solution(m, n, board) {
  var answer = 0
  const arr = Array.from(Array(n), () => Array(m).fill(0))
  
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      arr[i][j] = board[j][0]
      board[j] = board[j].slice(1,)
    }
  }
  
  const temp_board = new Array(n).fill(0)
  
  while (true) {
    const temp = Array.from(Array(n), () => Array(m).fill(0))
    
    for (let i = 0; i < n-1; i++) {
      for (let j = 0; j < m-1; j++) {
        if (arr[i][j] != '' && arr[i][j] == arr[i+1][j] && arr[i][j] == arr[i][j+1] && arr[i][j] == arr[i+1][j+1]) {
          temp[i][j] += 1
          temp[i][j+1] += 1
          temp[i+1][j] += 1
          temp[i+1][j+1] += 1
        }
      }
    }
    
    var isBreak = true
    
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (temp[i][j] != 0) {
          arr[i][j] = ''
          isBreak = false
        }
      }
    }
    
    if (isBreak) {
      break
    }
    
    for (let i = 0; i < n; i++) {
      temp_board[i] = arr[i].join('')
    }
    
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (j < m - temp_board[i].length) {
          arr[i][j] = ''
        } else {
          arr[i][j] = temp_board[i][0]
          temp_board[i] = temp_board[i].slice(1,)
        }
      }
    }
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (arr[i][j] === '') {
        answer += 1
      }
    }
  }
  return answer
}

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(m,n,board)
m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
solution(m,n,board)