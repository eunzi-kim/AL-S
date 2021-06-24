function solution(n) {
  var answer = ''
  var role = ['4', '1', '2']
  var arr = []
  while (n) {
    var temp = n % 3
    arr.push(role[temp])
    n = parseInt(n / 3)
    if (temp == 0) {
      n -= 1
    }
  }
  arr.reverse()
  answer = arr.join('')
  return answer
}