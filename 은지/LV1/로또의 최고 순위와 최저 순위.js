function solution(lottos, win_nums) {
  var chk = 0
  var zero = 0
  for (let x of lottos) {
    for (let y of win_nums) {
      if (x === y) {
        chk += 1
      }
    }
    if (x === 0) {
      zero += 1
    }
  }
  var minR = 0
  var maxR = 0
  if (chk >= 2) {
    minR = 7 - chk
  } else {
    minR = 6
  }
  if (chk+zero >= 2) {
    maxR = 7 - (chk + zero)
  } else {
    maxR = 6
  }
  var answer = [maxR, minR]
  return answer;
}