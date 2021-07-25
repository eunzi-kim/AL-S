function solution(name) {
  var answer = 0;
  const alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  for (let x of name) {
    for (let i=0; i<26; i++) {
      if (x === alpha[i]) {
        answer += Math.min(i, 26-i)
        break
      }
    } 
  }

  var min_v = 100
  for (let j=0; j<name.length; j++) {
    var e = j+1
    if (j+1 < name.length && name[j+1] === "A") {
      for (let k=j+2; k<name.length; k++) {
        if (name[k] !== "A") {
          e = k
          break
        }
      }
    }
    var len = Math.min(j*2 + (name.length-e), j+(name.length-e)*2)
    if (min_v > len) {
      min_v = len
    }     
  }

  answer += min_v

  return answer;
}

name = "JAZ"
console.log(solution(name))