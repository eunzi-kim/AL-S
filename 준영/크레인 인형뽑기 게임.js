function solution(board, moves) {
  var answer = 0;
  const length = board.length
  const depth = Array.from({length: length}, () => 0)
  
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][i]) {
        depth[i] = length - j
        break
      }
    }
  }
  console.log(depth)
  const stack = []

  moves.forEach((element) => {
    if (depth[element-1]) {
      if (stack.length && stack[stack.length-1] === board[length-depth[element-1]][element-1]) {
        stack.pop()
        answer += 2
      } else {
        stack.push(board[length-depth[element-1]][element-1])
      }
      depth[element-1] -= 1
    }
  });

  return answer;
}

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])