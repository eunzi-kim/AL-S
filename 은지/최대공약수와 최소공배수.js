function solution(n, m) {
  const min_v = Math.min(n, m)
  const max_v = Math.max(n, m)
  for (let x=0; x<=max_v*min_v; x++) {
    // 최대공약수
    if (min_v % x === 0 && max_v % x === 0) {
      var g = x
    }
    // 최소공배수
    if (x % min_v === 0 && x % max_v === 0) {
      var l = x
    }
    // 최소공배수 구해지면 멈춰!
    if (l) {
      break
    }
  }
  const answer = [g, l]
  return answer;
}