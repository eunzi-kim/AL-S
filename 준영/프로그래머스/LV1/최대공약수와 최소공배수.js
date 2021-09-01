function gcd(x, y) {
  var temp
  while ((x % y) > 0) {
    temp = x % y
    x = y
    y = temp
  }
  return y
}

function solution(n, m) {
  var gcd_temp = gcd(n, m)
  var lcm_temp = parseInt((n * m) / gcd_temp)
  var answer = [gcd_temp, lcm_temp]
  return answer
}