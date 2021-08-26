function solution(arr1, arr2) {
  var N = arr1.length
  var M = arr1[0].length
  var N1 = arr2.length
  var M1 = arr2[0].length
  
  var answer = Array.from(Array(N), () => Array(M1).fill(0))

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M1; j++) {
      var temp = 0
      for (let k = 0; k < M; k++) {
        temp += arr1[i][k] * arr2[k][j] 
      }
      answer[i][j] = temp
    }
  }
  return answer
}