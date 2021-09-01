const dict = ["0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

function solution(msg) {
  var answer = [];
  var i = 0
  var past = 0
  while (i<msg.length) {
    for (let j=i+1; j<=msg.length; j++) {
      if (dict.includes(msg.slice(i, j))) {
        past = dict.indexOf(msg.slice(i, j))
        if  (j === msg.length) {
          answer.push(past)
          i = j
        }
      } else {
        answer.push(past)
        dict.push(msg.slice(i, j))
        i = j-1
        break
      }
    }
  }
  return answer;
}