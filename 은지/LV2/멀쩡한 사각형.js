function solution(w, h) {
  // 최대공약수
  var g = 0
  for (let x=1; x<=w; x++) {
    if (w % x === 0 && h % x === 0) {
      g = x
    }
  }
  const answer = (w * h) - (w + h - g)
  return answer;
}