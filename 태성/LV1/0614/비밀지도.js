const n = 5
const arr1 = [9, 20, 28, 18, 11]
const arr2 = [30, 1, 21, 17, 28]

function solution(n, arr1, arr2) {
  var answer = [];

  var board1 = []
  for (let a1 of arr1) {
    // console.log(a1.toString(2))
    var aa1 = a1.toString(2)

    var pre1 = []
    for (let aaa1 of aa1) {
      pre1.push(aaa1)
    }

    if (pre1.length <n) {
      var d = n - pre1.length
      for (let i=0; i<d; i++) {
        pre1.unshift('0')
      }
    }

    // console.log(pre)
    board1.push(pre1)

    var board2 = []
    for (let a2 of arr2) {
      // console.log(a1.toString(2))
      var aa2 = a2.toString(2)
  
      var pre2 = []
      for (let aaa2 of aa2) {
        pre2.push(aaa2)
      }
  
      if (pre2.length <n) {
        var d = n - pre2.length
        for (let i=0; i<d; i++) {
          pre2.unshift('0')
        }
      }
      board2.push(pre2)

      
    }
  }
  


  console.log(board1)
  console.log(board2)

  
  for (let i=0; i<n; i++) {
    var pre_answer = ''
    for (let j=0; j<n; j++) {
      if(board1[i][j] === '1'|| board2[i][j] === '1'){
        pre_answer += '#'
        // console.log(10)
      } else {
        pre_answer += ' '
      }
    }
    console.log(pre_answer)
    answer.push(pre_answer)
  }
  // console.log(answer)
  return answer;
}

console.log(solution(n, arr1, arr2))