function solution(d, budget) {
  var answer = 0;
  const d_sort = d.sort((a, b) => a-b)
  for (let x of d_sort) {
    if (budget >= x) {
      budget -= x
      answer += 1 
    }
  }
  return answer;
}