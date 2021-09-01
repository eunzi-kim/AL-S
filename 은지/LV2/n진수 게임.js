function solution(n, t, m, p) {
  var answer = '';
  var all_ans = ''
  var i = 0
  while (all_ans.length <= t*m) {
    all_ans += i.toString(n)
    i += 1
  }
  
  var j = p-1
  while (answer.length < t) {
    answer += all_ans[j]
    j += m
  }
  return answer.toUpperCase();
}