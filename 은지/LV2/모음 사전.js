function solution(word) {
  let answer = 0;
  let info = ["A", "E", "I", "O", "U"]

  for (let i=0; i<word.length; i++) {
    if (word[i] === "A") {
      answer += 1
    } 
    else {
      let idx = info.indexOf(word[i])
      answer += idx + 1
      for (let j=i+1; j<5; j++) {
        answer += (5 ** (5-j)) * idx
      }
    }
  }

  return answer;
}