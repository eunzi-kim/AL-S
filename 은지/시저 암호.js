function solution(s, n) {
  var answer = '';
  const Upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  const Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for (let x of s) {
    // 공백
    if (x === ' ') {
      answer += ' '
    }
    // 1. 대문자
    else if (Upper.indexOf(x) !== -1) {
      // 다시 돌아가야하는 경우
      if (Upper.indexOf(x) + n >= 26) {
        answer += Upper[Upper.indexOf(x)+n-26]
      } 
      // 돌아갈 필요없는 경우
      else {
        answer += Upper[Upper.indexOf(x)+n]
      }      
    }
    // 2. 소문자
    else {
      // 다시 돌아가야하는 경우
      if (Lower.indexOf(x) + n >= 26) {
        answer += Lower[Lower.indexOf(x)+n-26]
      } 
      // 돌아갈 필요없는 경우
      else {
        answer += Lower[Lower.indexOf(x)+n]
      }
    }
  }
  return answer;
}