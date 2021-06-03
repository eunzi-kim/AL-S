function solution(array, commands) {
    var answer = [];
    for (let j=0; j < commands.length; j++) {
      var sub_a = []
      for (let i=0; i < array.length; i++) {
        sub_a = array.slice(commands[j][0]-1, commands[j][1])
      }
      sub_a.sort((a, b) => a-b)
      answer.push(sub_a[commands[j][2]-1])
      sub_a = []
    }
    return answer;
}

array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
console.log(solution(array, commands))