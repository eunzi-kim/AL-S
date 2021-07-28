function solution(citations) {
  var answer = 0
  var pre = []
  var arr = Array.from({length: 10000}, (v, i) => 0)
  // console.log(arr)

  for (let i=0; i<citations.length; i++) {
      let cnt = 0
      for (let j=0; j<citations.length; j++) {
          if (citations[i]<=citations[j]) {
              cnt ++
          }
      }
      if (citations[i] <= cnt) {
          pre.push(citations[i])
      } else {
          pre.push(cnt)
      }
  }
  answer = Math.max(...pre)
  return answer
}