function solution(maps) {
  var answer = 0
  var n = maps.length
  var m = maps[0].length
  var visited = Array.from(Array(n), () => new Array(m).fill(0))
  var my_queue = []
  my_queue.push([0, 0, 1])
  visited[0][0] = 1
  var dx = [-1, 1, 0, 0]
  var dy = [0, 0, -1, 1]

  while (my_queue.length != 0) {
    var temp = my_queue.shift()
    var x = temp[0]
    var y = temp[1]
    var d = temp[2]

    for (let i = 0; i < 4; i++) {
      var vx = x + dx[i]
      var vy = y + dy[i]

      if (vx < 0 || vy < 0 || vx >= n || vy >= m) {
        continue
      }

      if (visited[vx][vy]) {
        continue
      }

      if (maps[vx][vy] == 0) {
        continue
      }

      visited[vx][vy] = d+1

      my_queue.push([vx, vy, d+1])
    }
  }
  answer = visited[n-1][m-1]
  if (answer === 0) {
    answer = -1
  }
  return answer
}