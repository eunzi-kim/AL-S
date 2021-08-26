function solution(record) {
  var record_dict = {}
  var answer1 = []
  var answer2 = []
  var answer = []

  for (const i of record) {
    var temp = i.split(' ')
    if (temp[0] === 'Enter') {
      record_dict[temp[1]] = temp[2]
      answer1.push(temp[1])
      answer2.push('님이 들어왔습니다.')
    } else if (temp[0] === 'Leave') {
      answer1.push(temp[1])
      answer2.push('님이 나갔습니다.')
    } else if (temp[0] === 'Change') {
      record_dict[temp[1]] = temp[2]
    }
  }

  for (let i = 0; i < answer1.length; i++) {
    answer.push(record_dict[answer1[i]] + answer2[i])
  }

  return answer
}


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	

console.log(solution(record))
