function solution(N, stages) {
  var answer = [];
  // 실패율 리스트
  var fail = []
  // 사용자수
  let m = stages.length
  for (let n=0; n < N; n++) {
    // 스테이지에 도달한 사람의 수가 0인 경우
    if (m === 0) {
      fail.push(0)
      // 스테이지에 도달한 사람의 수가 0이 아닌 경우
    } else {
      // 현재 단계에 있는 사람의 수
      let lv = stages.filter(ele => n+1 === ele).length
      fail.push(lv/m)
      m -= lv
    }
  }
  // 정렬
  for (let i=0; i<N; i++) {
    // 가장 큰 실패율의 인덱스
    var idx = fail.indexOf(Math.max(...fail))
    answer.push(idx+1)
    // 사용한 실패율 제거
    fail[idx] = -1
  }
  return answer;
}