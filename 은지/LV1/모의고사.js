function solution(answers) {
  var answer = []
  const N = answers.length
  // A, B, C의 답안
  var A = []
  for (let i = 0; i < N; i++) {
    A.push(i%5+1)
  }
  var B = []
  const b = [1, 3, 4, 5]
  for (let i = 0; i < N/2+1; i++) {
    B.push(2)
    B.push(b[i%4])
  }
  var C = []
  const c = [3, 1, 2, 4, 5]
  for (let i = 0; i < N/2+1; i++) {
    C.push(c[i%5])
    C.push(c[i%5])
  }
  // 답 체크
  var Check = [0, 0, 0]
  for (let i = 0; i < N; i++) {
    if (A[i] === answers[i]) {
      Check[0] += 1
    }
    if (B[i] === answers[i]) {
      Check[1] += 1
    }
    if (C[i] === answers[i]) {
      Check[2] += 1
    }
  }
  // 가장 높은 점수
  const maxV = Math.max(...Check)
  // 가장 높은 점수 학생 탐색
  for (let i=0; i<3; i++) {
    if (Check[i] === maxV) {
      answer.push(i+1)
    }
  }  
  return answer;
}