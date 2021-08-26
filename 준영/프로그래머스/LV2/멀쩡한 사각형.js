function gcd(x, y) {
  var temp
  while ((x % y) > 0) {
    temp = x % y
    x = y
    y = temp
  }
  return y
}

function solution(w, h) {
  var answer = w * h - w - h + gcd(w, h)
  return answer
}