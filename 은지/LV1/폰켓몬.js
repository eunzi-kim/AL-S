function solution(nums) {
  var answer = 0
  const N = nums.length / 2
  var mon = []
  for (let x of nums) {
    if (!mon.includes(x)) {
      mon.push(x)
    }
  }
  if (mon.length < N) {
    answer = mon.length
  } else {
    answer = N
  }
  return answer;
}