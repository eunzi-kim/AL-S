function solution(dartResult) {
  // 점수 리스트
  var score = []
  // 숫자 점수
  var sub_s = ''
  for (let x of dartResult) {
    // 숫자 점수를 문자열 => 숫자 변경
    if (sub_s.length > 0) {
      var sub_v = Number(sub_s)
    }
    // 스타상
    if (x === '*') {
      if (score.length > 1) {
        var v2 = score.pop()
        var v1 = score.pop()
        v1 *= 2
        score.push(v1)
        v2 *= 2
        score.push(v2)
      }
      else if (score.length === 1) {
        var v3 = score.pop()
        v3 *= 2
        score.push(v3)
      }
    }
    // 아차상
    else if (x === '#') {
      var v = score.pop()
      v *= -1
      score.push(v)
    }
    // Single, Double, Triple
    else if (x  === 'S' || x === 'D' || x === 'T') {
      if (x === 'S') {
        sub_v **= 1
      }
      else if (x === 'D') {
        sub_v **= 2
      }
      else if (x === 'T') {
        sub_v **= 3
      }
      score.push(sub_v)
      sub_s = ''
      sub_v = 0
    }
    // 숫자 입력
    else {
      sub_s += x
    }
  }
  // 모든 점수의 합
  const answer = score.reduce((a, b) => a+b, 0)
  return answer;
}