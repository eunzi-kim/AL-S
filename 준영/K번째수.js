function solution(array, commands) {
  var answer = []

  for (const command of commands) {
    answer.push(array.slice(command[0]-1, command[1]).sort((a, b) => {
      return a - b
    })[command[2]-1])
  }

  return answer
}


var array = [1, 5, 2, 6, 3, 7, 4]
var commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array, commands)
console.log(solution(array, commands))