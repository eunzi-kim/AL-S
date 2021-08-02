function solution(numbers) {
  var answer = [];
  for (let number of numbers) {
    if (number % 2 === 0) {
      answer.push(number+1)
    } 
    else {
      var two_n = number.toString(2)
      var one_cnt = 0 
      var v = ""
      for (let x of two_n) {
        if (x === "1") {
          one_cnt += 1
        }
      }
      if (two_n.length === one_cnt) {
        v = "10" + two_n.slice(1)
      } 
      else {
        for (let i=(two_n.length)-1; i>=0; i--) {
          if (two_n[i-1] === "0" && two_n[i] === "1") {
            v = two_n.slice(0, i-1) + "10" + two_n.slice(i+1)
            break
          }
        }
      }
      var val = 0
      for (let j=(v.length)-1; j>=0; j--) {
        val += parseInt(v[j]) * (2 ** ((v.length)-j-1))
      }
      answer.push(val)
    }
  }
  return answer;
}