function solution(msg) {
  var answer = []
  var  alphabat = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
  }

  var x = 27
  var idx = 0
  
  while (idx < msg.length) {
    for (let i = msg.length; i > idx; i--) {
      if (msg.substring(idx, i - idx - 1) in alphabat) {
        console.log(msg.substring(idx, i - idx - 1))
        answer.push(alphabat[msg.substring(idx, i - idx - 1)])
        alphabat[msg.substring(idx, i - idx)] = x
        x += 1
        idx += msg.substring(idx, i - idx - 1).length
        break
      }
    }
    console.log(answer)
  }
  return answer
}

msg = 'KAKAO'
solution(msg)
// msg = 'TOBEORNOTTOBEORTOBEORNOT'
// solution(msg)
// msg = 'ABABABABABABABAB'
// solution(msg)


