function solution(nums) {
  var answer = 0
  const set_nums = new Set(nums)
  var n = nums.length
  var m = set_nums.size
  if (n/2 < m) {
    answer = n/2
  } else {
    answer = m
  }
  return answer
}


nums = [3, 1, 2, 3]
console.log(solution(nums))