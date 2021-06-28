var result = 0

function dfs(n, numbers, d, target) {
  if (n === numbers.length) {
    if (d === target) {
      result += 1
    }
  } else {
    for (const i of [-1, 1]) {
      dfs(n+1, numbers, d+(numbers[n]*i), target)
    }
  }
}

function solution(numbers, target) {
  dfs(0, numbers, 0, target)
  var answer = result
  return answer
}