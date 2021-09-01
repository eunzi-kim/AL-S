function is_numeric(str){
  return /^\d+$/.test(str);
}

function solution(dartResult) {
  var answer = 0
  var idx = 1
  var last = 0
  var n = dartResult.length
  var arr = []
  while (idx < n) {
    if (is_numeric(dartResult[idx])) {
      if (dartResult[idx] === '0' && dartResult[idx-1] == '1') {

      } else {
        arr.push(dartResult.slice(last,idx))
        last = idx
      }
    }
    if (arr.length === 2) {
      break
    }
    idx += 1
  }
  
  arr.push(dartResult.slice(idx,))

  var score = 0
  var score_arr = [0, 0, 0]

  for (let i = 0; i < 3; i++) {
    if (arr[i][0] == '1' && arr[i][1] == '0') {
      score = 10
      arr[i] = '0' + arr[i].slice(2)
    } else {
      score = parseInt(arr[i][0])
    }
    
    if (arr[i][1] === 'S') {
      score **= 1
    } else if (arr[i][1] === 'D') {
      score **= 2
    } else {
      score **= 3
    }

    if (arr[i].length >= 3) {
      if (i > 0 && arr[i][2] === '*') {
        score_arr[i-1] *= 2
        score *= 2
      } else if (i === 0 && arr[i][2] === '*') {
        score *= 2
      }

      if (arr[i][2] === '#') {
        score *= -1
      }
    }
    score_arr[i] = score
  }

  for (let i = 0; i < 3; i++) {
    answer += score_arr[i]
  }

  return answer
}

console.log(solution('1S2D*3T'))
console.log(solution('1D2S#10S'))
console.log(solution('1D2S0T'))
console.log(solution('1S*2T*3S'))
console.log(solution('1D#2S*3S'))
console.log(solution('1T2D3D#'))
console.log(solution('1D2S3T*'))
console.log(solution('10D2S3T*'))