function solution(numbers, hand) {
  var answer = '';
  // 번호별 위치
  const pos = {
    1: [0, 0], 2: [1, 0], 3: [2, 0],
    4: [0, 1], 5: [1, 1], 6: [2, 1],
    7: [0, 2], 8: [1, 2], 9: [2, 2],
    0: [1, 3]
  }
  // 현재 손가락의 위치
  var L = [0, 3]
  var R = [2, 3]
  for (let number of numbers) {
    // 1, 4, 7 입력
    if (number === 1 || number === 4 || number === 7) {
      L = pos[number]
      answer += "L"
    }
    // 3, 6, 9 입력
    else if (number === 3 || number === 6 || number === 9) {
      R = pos[number]
      answer += "R"
    }
    // 2, 5, 8, 0 입력
    else {
      // 왼손이 더 가까운 경우
      if (Math.abs(pos[number][0]-L[0]) + Math.abs(pos[number][1]-L[1]) < Math.abs(pos[number][0]-R[0]) + Math.abs(pos[number][1]-R[1])) {
        L = pos[number]
        answer += "L"
      } 
      // 오른손이 더 가까운 경우
      else if (Math.abs(pos[number][0]-L[0]) + Math.abs(pos[number][1]-L[1]) > Math.abs(pos[number][0]-R[0]) + Math.abs(pos[number][1]-R[1])) {
        R = pos[number]
        answer += "R"
        // 거리가 같은 경우
      } else {
        if (hand === "left") {
          L = pos[number]
          answer += "L"
        } else {
          R = pos[number]
          answer += "R"
        }
      }
    }
  }
  return answer;
}