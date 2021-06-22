function solution(n) {
  // 배수 확인 배열
  var check = []
  for (let i=0; i<=n; i++) {
    check.push(0)
  }
  // 소수 배열
  var prime = []
  for (let x=2; x<=n; x++) {
    // x가 소수
    if (check[x] === 0) {
      // 소수 리스트 추가
      prime.push(x)
      // x의 배수 체크
      for (let y=x; y<=n; y+=x) {
        check[y] = 1
      }
    }
  }
  // 소수 개수
  const answer = prime.length
  return answer;
}