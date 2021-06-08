const keypad = [[3, 1]]

for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    keypad.push([i, j])
  }
}

const left_keypad = [1, 4, 7]
const right_keypad = [3, 6, 9]
const center_keypad = [2, 5, 8, 0]

function solution(numbers, hand) {
  var x = ""
  var y = ""
  var answer = ''
  var left_hand = [3, 0]
  var right_hand = [3, 2]

  for (const n of numbers) {
    [x, y] = keypad[n]
    if (center_keypad.includes(n)) {
      const left_d = Math.abs(left_hand[0] - x) + Math.abs(left_hand[1] - y)
      const right_d = Math.abs(right_hand[0] - x) + Math.abs(right_hand[1] - y)
      
      if (left_d < right_d) {
        left_hand = [x, y]
        answer += "L"
      } else if (left_d > right_d) {
        right_hand = [x, y]
        answer += "R"
      } else {
        if (hand === "right") {
          right_hand = [x, y]
          answer += "R"
        } else {
          left_hand = [x, y]
          answer += "L"
        }

      }

    } else if (left_keypad.includes(n)) {
      left_hand = [x, y]
      answer += "L"
    } else {
      right_hand = [x, y]
      answer += "R"
    }
  } 


  return answer
}


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
console.log(solution(numbers, hand))