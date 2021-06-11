function solution(n) {
  // 10진법 -> 3진법
    const t = n.toString(3)

  // 10진법 변환
  var answer = 0
  for (let i=0; i<t.length; i++) {
    answer += Number(t[i]) * (3 ** i)
  }
  return answer;
}