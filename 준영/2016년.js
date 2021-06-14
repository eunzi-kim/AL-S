function solution(a, b) {
  const week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
  const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  var answer = ''
  var result = 0

  for (let i = 0; i < a-1; i++) {
    result += month[i]
  }

  result += b
  answer = week[(result-1)%7]
  
  return answer;
}