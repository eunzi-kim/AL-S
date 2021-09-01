function solution(number, k) {
  var answer = '';
  var i = 0;
  while (answer.length < number.length - k) {
    var max_v = 0
    for (let j=i; j<k+1+answer.length; j++) {
      if (Number(number[j]) === 9) {
        max_v = Number(number[j])
        i = j + 1
        break
      }
      if (Number(number[j]) > max_v) {
        max_v = Number(number[j])
        i = j + 1
      }
    }
    answer += String(max_v)
  }
  return answer;
}