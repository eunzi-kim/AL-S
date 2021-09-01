function solution(n, t, m, p) {
  var answer = ''
  var arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
  const result = [0]

  for (let i = 1; i < m*t+1; i++) {
    const temp = Array(0)
    var idx = i
    while (idx) {
      temp.unshift(arr[idx % n])
      idx = parseInt(idx / n)
    }

    for (const j of temp) {
      result.push(j)
      if (result.length >= m*t) {
        break
      }
    }
    if (result.length >= m*t) {
      break
    }  
  }
  
  for (let i = p-1; i < result.length; i += m) {
    answer += String(result[i])     
  }
  return answer
}

n = 2
t = 4
m = 2
p = 1
solution(n, t, m, p)
n = 16
t = 16
m = 2
p = 1
solution(n, t, m, p)