function solution(n) {
  var answer = 0
  var arr = Array.from({length: n+1}, x => true)
  var m = parseInt(n ** 0.5)
  for (let i = 2; i < m+1; i++) {
    if (arr[i] === true) {
      for (let j = i*i; j < n+1; j += i) {
        arr[j] = false
      }
    }
  }
  answer = arr.reduce((acc, cur) => {
    if (cur === false) {
      return acc
    } else {
      return acc + 1
    }
  }, -2)

  return answer 
}

solution(10)