function solution(rows, columns, queries) {
  var answer = []
  var init_arr = Array.from(Array(rows), () => new Array(columns).fill(0))
  for (let i = 1; i <= rows; i++) {
    for (let j = 1; j <= columns; j++) {
      init_arr[i-1][j-1] = (i-1)*columns + j
    }
  }
  for (const query of queries) {
    var temp = Array.from(Array(rows), () => new Array(columns).fill(0))
    var arr = []
    var start_x = query[0]
    var start_y = query[1]
    var end_x = query[2]
    var end_y = query[3]

    for (let j = start_y; j < end_y; j++) {
      temp[start_x-1][j] = init_arr[start_x-1][j-1]
      arr.push(temp[start_x-1][j])
    }
    
    for (let i = start_x; i < end_x; i++) {
      temp[i][end_y-1] = init_arr[i-1][end_y-1]
      arr.push(temp[i][end_y-1])
    }
    
    for (let j = start_y; j < end_y; j++) {
      temp[end_x-1][j-1] = init_arr[end_x-1][j]
      arr.push(temp[end_x-1][j-1])
    }
    
    for (let i = start_x; i < end_x; i++) {
      temp[i-1][start_y-1] = init_arr[i][start_y-1]
      arr.push(temp[i-1][start_y-1])
    }

    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < columns; j++) {
        if (temp[i][j] != 0) {
          init_arr[i][j] = temp[i][j]
        }
      }
    }
    answer.push(Math.min(...arr))
  }

  console.log(answer)
  return answer
}

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)
rows = 100
columns = 97
queries = [[1,1,100,97]]	
solution(rows, columns, queries)