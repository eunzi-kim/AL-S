function solution(n,a,b)
{
    var answer = 0;
    var person = []
    for (let x=1; x<=n; x++) {
      person.push(x)
    }
    while (person.length) {
      var winner = []
      for (let i=0; i<person.length; i+=2) {
        const p1 = person[i]
        const p2 = person[i+1]
        if (p1 === a || p2 === b) {
          if (p1 === a && p2 === b) {
            return answer + 1
          } else if (p2 !== b) {
            winner.push(p1)
          } else if (p1 !== a) {
            winner.push(p2)
          }
        } else if (p1 === b || p2 === a) {
          if (p1 === b && p2 === a) {
            return answer + 1
          } else if (p2 !== a) {
            winner.push(p1)
          } else if (p1 !== b) {
            winner.push(p2)
          }
        } else {
          winner.push(p1)
        }
      }
      answer += 1
      person = winner.slice(0, winner.length)
    }
    return answer;
}