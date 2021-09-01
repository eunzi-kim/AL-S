function solution(nums) {
  var answer = 0
  // 소수 구하기
  var prime = []
  const m = Math.max(...nums) * 3
  var chk = [2]
  for (let i=0; i<m+1; i++) {
    chk.push(1)
  }
  for (let i=3; i<m+1; i+=2) {
    if (chk[i]) {
      prime.push(i)
      for (let j=i; j<m+1; j+=i) {
        chk[j] = 0
      }
    }
  }

  // 주어진 숫자 3개 조합
  for (let i=0; i<nums.length; i++) {
    for (let j=i+1; j<nums.length; j++) {
      for (let k=j+1; k<nums.length; k++) {
        var sub_v = nums[i] + nums[j] + nums[k]
        // 소수가 되는 경우
        if (prime.includes(sub_v)) {
          answer += 1
        }
      }
    }
  }
  return answer;
}