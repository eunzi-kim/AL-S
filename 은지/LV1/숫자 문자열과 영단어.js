function solution(s) {
    var answer = 0;
    const num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    var n = ""
    for (let v of s) {
      if (isNaN(v)) {
        n += v
      } else {
        answer += v
      }

      for (let i=0; i<10; i++) {
        if (n === num[i]) {
          answer += String(i)
          n = ""
          break
        }
      }
    }
    answer = Number(answer)
    return answer;
}

s = "zeroone"
console.log(solution(s))