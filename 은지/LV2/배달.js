function solution(N, road, K) {
  var answer = 0;
  var g = new Array(N+1)
  for (let i=0; i<N+1; i++) {
    g[i] = []
  }
  for (let r of road) {
    g[r[0]].push(r)
    g[r[1]].push([r[1], r[0], r[2]])
  }

  var d = []
  for (let i=0; i<N+1; i++) {
    d[i] = 500001
  }

  var queue = g[1]
  d[1] = 0

  while (queue.length) {
    var v = queue.shift()
    var s = v[0]
    var e = v[1]
    var dis = v[2]
    if (d[e] > d[s] + dis) {
      d[e] = d[s] + dis
      for (let w of g[e]) {
        queue.push(w)
      }
    }
  }
  
  for (let i=1; i<N+1; i++) {
    if (d[i] <= K) {
      answer += 1
    }
  }
  return answer;
}

n = 5
r = [[2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2], [1, 2, 1] ]
k = 3
console.log(solution(n, r, k))