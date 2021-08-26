function solution(s) {
  var answer = ''
  var dic = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,	
    'seven': 7,
    'eight': 8,
    'nine': 9,
  }
  var temp = ''
  for (const i of s) {
    if (!isNaN(i)) {
      answer += i
    } else {
      temp += i

      if (temp in dic) {
        answer += String(dic[temp])
        temp = ''
      }
    }
  }
  return parseInt(answer)
}