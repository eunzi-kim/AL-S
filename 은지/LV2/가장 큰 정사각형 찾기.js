function solution(board)
{
    var answer = 0;
    const n = board.length
    const m = board[0].length

    if (n === 1 && m === 1 && board[0][0] === 1) {
      return 1
    }

    for (let i=1; i<n; i++) {
      for (let j=1; j<m; j++) {
        if (board[i][j]) {
          board[i][j] = Math.min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
          if (answer < board[i][j]) {
            answer = board[i][j]
          }
        }
      }
    }

    return answer ** 2;
}