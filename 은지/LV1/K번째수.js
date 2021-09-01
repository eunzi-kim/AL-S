function solution(array, commands) {
    var answer = [];
    for (let j=0; j < commands.length; j++) {
      var sub_a = array.slice(commands[j][0]-1, commands[j][1])
      sub_a.sort((a, b) => a-b)
      answer.push(sub_a[commands[j][2]-1])
      sub_a = []
    }
    return answer;
}