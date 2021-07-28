function solution(people, limit){
	var answer = 0
  people.sort((a,b) => b-a)
  let l = 0
  let r = people.length-1
  
  while(l<r){
    var sum = people[l] + people[r]
    if(sum>limit){
      l += 1
    } else {
      l += 1
      r -= 1
    }
    answer += 1
  }
  if (l == r) answer += 1
  return answer
}