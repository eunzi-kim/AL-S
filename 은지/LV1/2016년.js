function solution(a, b) {
  var answer = '';
  const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  const week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
  var day = b-1
  for (let i=0; i<a-1; i++) {
    day += month[i]
  }
  day %= 7
  answer = week[day]
  return answer;
}