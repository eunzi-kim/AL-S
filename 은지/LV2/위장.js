function solution(clothes) {
  var answer = 1;
  var sorts = {}
  for (let c of clothes) {
    if (sorts[c[1]]) {
      sorts[c[1]] += 1
    } else {
      sorts[c[1]] = 1
    }
  }

  for (let sort in sorts) {
    answer *= sorts[sort]+1
  }
  
  answer -= 1
  return answer;
}