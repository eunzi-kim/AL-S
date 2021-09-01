function rotation(info, m, min_v) {
    const r1 = info[0]-1
    const c1 = info[1]-1
    const r2 = info[2]-1
    const c2 = info[3]-1
    for (let i=c1; i<c2; i++) {
      var v = m[r1][i].shift()
      m[r1][i+1].push(v)
      if (min_v > v) {
        min_v = v
      }
    }
    for (let i=r1; i<r2; i++) {
      var v = m[i][c2].shift()
      m[i+1][c2].push(v)
      if (min_v > v) {
        min_v = v
      }
    }
    for (let i=c2; i>c1; i--) {
      var v = m[r2][i].shift()
      m[r2][i-1].push(v)
      if (min_v > v) {
        min_v = v
      }
    }
    for (let i=r2; i>r1; i--) {
      var v = m[i][c1].shift()
      m[i-1][c1].push(v)
      if (min_v > v) {
        min_v = v
      }
    }
  return min_v
}

function solution(rows, columns, queries) {
  var answer = [];
  var matrix = new Array(rows)
  for (let i=0; i<rows; i++) {
    matrix[i] = new Array(columns)
    for (let j=1; j<=columns; j++) {
      matrix[i][j-1] = [columns*i+j]
    }
  }
  for (let q of queries) {
    answer.push(rotation(q, matrix, rows*columns))
  }
  return answer;
}

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
console.log(solution(rows, columns, queries))