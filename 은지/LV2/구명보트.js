function solution(people, limit) {
    var answer = 0;
    people.sort((a, b) => a-b)
    var l = 0
    var r = people.length-1
    while (l<=r) {
      if (people[l]+people[r] <= limit) {
        l += 1
        r -= 1
        answer += 1
      } else {
        r -= 1
        answer += 1
      }
    }
    return answer;
}