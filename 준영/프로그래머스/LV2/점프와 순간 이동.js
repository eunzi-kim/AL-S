function solution(n) {
  var ans = 0

  while (n) {
    if (n % 2) {
      ans += 1
    }
    n = parseInt(n / 2)
  }
  return ans
}