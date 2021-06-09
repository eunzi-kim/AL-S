const numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
const hand = "right"

var board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [11, 0, 12],
]

function find_yx(board, a) {

  for (let b in board) {
    for (let c in board[b]) {
      if (board[b][c] === a) {
        return [b, c]
      }
    }
  }
}

function solution(numbers, hand) {
  var answer = '';
  var right_now = [3, 2]
  var left_now = [3, 0]
  const left_pad = [1, 4, 7]
  const right_pad = [3, 6, 9]

  for (let i in numbers) {
    if (left_pad.includes(numbers[i])) {
      answer += 'L'
      left_now = find_yx(board, numbers[i])
    } else if (right_pad.includes(numbers[i])) {
      answer += 'R'
      right_now = find_yx(board, numbers[i])
    } else {
      let n_y = find_yx(board, numbers[i])[0]
      let n_x = find_yx(board, numbers[i])[1]
      if (Math.abs(left_now[0] - n_y) + Math.abs(left_now[1] - n_x) > Math.abs(right_now[0] - n_y) + Math.abs(right_now[1] - n_x)) {
        answer += 'R'
        right_now = find_yx(board, numbers[i])
      } else if (Math.abs(left_now[0] - n_y) + Math.abs(left_now[1] - n_x) < Math.abs(right_now[0] - n_y) + Math.abs(right_now[1] - n_x)) {
        answer += 'L'
        left_now = find_yx(board, numbers[i])        
      } else {
        if (hand === 'right') {
          answer += 'R'
          right_now = find_yx(board, numbers[i])          
        } else{
          answer += 'L'
          left_now = find_yx(board, numbers[i]) 
        }

      }
    }
  }
  return answer;
}

// console.log(find_yx(board, 1))
console.log(solution(numbers, hand))