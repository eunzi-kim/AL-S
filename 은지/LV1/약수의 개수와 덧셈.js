function solution(left, right) {
  var answer = 0;
  for (let x=left; x<=right; x++) {
    // x의  약수의 개수 초기화
    var cnt = 0
    for (let y=1; y<=x; y++) {
      if(x%y === 0) {
        cnt += 1
      }
    }
    // 약수의 개수가 홀수
    if (cnt % 2) {
      answer -= x
    }
    // 약수의 개수가 짝수
    else {
      answer += x
    }
  }
  return answer;
}