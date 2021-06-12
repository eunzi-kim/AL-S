function solution(d, budget) {
  var answer = 0;
  d.sort(function(a,b) {
    return a - b
  })

  for (let i of d) {
    if(budget >= i){
      budget-=i
      answer+=1
    }
  }
  return answer;
}