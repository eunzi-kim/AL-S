function solution(numbers, target) {
  var answer = 0
  add(0, 0, numbers, target)
  function add(i, sumV, n, t) {
    if (i === n.length) {
      if (sumV === t) {
        answer += 1
      }      
    } else {
      add(i+1, sumV+n[i], n, t)
      add(i+1, sumV-n[i], n, t)
    }
  }
  return answer;
}

numbers = [1, 1, 1, 1, 1]
target = 3
console.log(solution(numbers, target))