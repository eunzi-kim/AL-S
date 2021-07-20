function solution(N, road, K) {
  var answer = 0

  var result_arr = new Array()
  result_arr.length = N+1
  result_arr.fill(500001)
  result_arr[1] = 0
  
  var road_two = Array.from(Array(N+1), () => new Array(N+1).fill(10001))

  for (const i of road) {
    if (road_two[i[0]][i[1]] > i[2]) {
      road_two[i[0]][i[1]] = i[2]
      road_two[i[1]][i[0]] = i[2]
    }
  }

  // dijkstra

  var my_queue = []
  my_queue.push([0, 1])

  while (my_queue.length > 0) {
    var x = my_queue.pop()
    var dist = x[0]
    var now = x[1]

    if (result_arr[now] < dist) {
      continue
    }

    for (let i = 1; i < N+1; i++) {
      if (road_two[now][i] < 10001) {
        var cost = dist + road_two[now][i]

        if (cost < result_arr[i]) {
          result_arr[i] = cost
          my_queue.push([cost, i])
        }
      }
    }
  }

  for (const i of result_arr) {
    if (i <= K) {
      answer += 1
    }
  }

  return answer
}

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
solution(N, road, K)