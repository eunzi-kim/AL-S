function to_bin(n, x) {
  var result = []
  for (let i = 0; i < n; i++) {
    if (parseInt(x / (2**(n-1-i))) === 1) {
      result.push("1")
    } else {
      result.push("0")
    }
    x %= (2**(n-1-i))
  }
  return result
}

function solution(n, arr1, arr2) {
  var answer = [];
  for (let i = 0; i < n; i++) {
    var temp = ""
    var x = to_bin(n, arr1[i])
    var y = to_bin(n, arr2[i])
    for (let j = 0; j < n; j++) {
      if (x[j] === '1' || y[j] === '1') {
        temp += "#"
      } else {
        temp += " "
      } 
    }
    answer.push(temp)
  }
  return answer;
}