function solution(n, words) {
  var answer = []
  var c = []
  var turn = 0
  var number = 0
  // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다. 
  // console.log('Hello Javascript')
  for (let i=0; i<words.length; i++) {
      if (c.includes(words[i]) === false) {
          if (c.length === 0) {
              c.push(words[i])
          } else {
              // console.log(c[c.length-1])
              // console.log(c[c.length-1].length-1)
              // console.log(c[c.length-1].substring(c[c.length-1].length-1, c[c.length-1].length))
              // console.log(c[c.length-1].substring(3,4))
              if (c[c.length-1].substring(c[c.length-1].length-1, c[c.length-1].length) === words[i].substring(0, 1)) {
                  c.push(words[i])
              } else {
                  turn = parseInt(i/n) +1
                  number = i%n +1
                  break
              }
          }

      } else {
          turn = parseInt(i/n) +1
          number = i%n +1
          break
      }
  }
  console.log(turn, number)
  answer.push(number)
  answer.push(turn)
  return answer
}