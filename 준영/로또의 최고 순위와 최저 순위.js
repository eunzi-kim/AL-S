function solution(lottos, win_nums) {
  var answer = []
  let zero_nums = lottos.filter(element => element === 0).length
  var result = 0
  for (const lotto of lottos) {
    if (win_nums.indexOf(lotto) != -1) {
      result += 1
    }
  }

  if (7-(result+zero_nums) > 6) {
    var best_win = 6
  } else {
    var best_win = 7-(result+zero_nums)
  }

  if (7-result > 6) {
    var worst_win = 6
  } else {
    var worst_win = 7-result
  }

  answer.push(best_win)
  answer.push(worst_win)
  return answer
}

var lottos = [44, 1, 0, 0, 31, 25]
var win_nums = [31, 10, 45, 1, 6, 19]
console.log(solution(lottos, win_nums))

var lottos = [0, 0, 0, 0, 0, 0]	
var win_nums = [38, 19, 20, 40, 15, 25]
console.log(solution(lottos, win_nums))

var lottos = [45, 4, 35, 20, 3, 9]	
var win_nums = [20, 9, 3, 45, 4, 35]
console.log(solution(lottos, win_nums))
