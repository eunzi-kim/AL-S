var board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
const moves = [1,5,3,5,1,2,1,4]


function solution(board, moves) {
  var answer = 0;
  // console.log(board)
  // console.log(moves)
  var pre = [0]
  for (let m of moves) {
    for (let i in board) {
      if (board[i][m-1] !== 0) {
        if (board[i][m-1] === pre[pre.length-1]) {
          pre.pop()
          answer += 2
        } else {
          pre.push(board[i][m-1])
        }
        
        board[i][m-1] = 0
        break
      }
    }

    
  }
  return answer;
}


console.log(solution(board, moves))
