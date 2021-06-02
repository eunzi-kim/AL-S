function solution(board, moves) {
    let answer = 0
    const N = board.length
    const basket = []
    for (let x of moves) {
      for (let i = 0; i < N; i++ ) {
        if (board[i][x-1] !== 0) {
          basket.push(board[i][x-1])
          board[i][x-1] = 0
          break;
        }
      }
      if(basket.length > 1 && basket[basket.length-1] === basket[basket.length-2]) {        
        basket.pop()
        basket.pop()
        answer += 2
      }
    }
    return answer;
}

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
console.log(solution(board, moves))