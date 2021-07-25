function solution(n, lost, reserve) {
    var answer = 0;
    var cloth = []
    for (let i=0; i<=n; i++) {
      cloth.push(1)
    }
    
    for (let i of lost) {
      cloth[i] -= 1
    }

    for (let i of reserve) {
      cloth[i] += 1
    }

    for (let i=0; i<=n; i++) {
      if (i-1>0 && cloth[i] === 2 && cloth[i-1] === 0) {
        cloth[i-1] = 1
        cloth[i] = 1
      }
      else if (i+1<=n && cloth[i] === 2 && cloth[i+1] === 0) {
        cloth[i+1] = 1
        cloth[i] = 1
      }
    }
    
    for (let i=1; i<n+1; i++) {
      if (cloth[i]) {
        answer += 1
      }
    }
    return answer
  }
n = 10
l = [8, 10]
r = [6, 7, 9]
console.log(solution(n, l, r))