function solution(s) {
  var zero = 0
  var cnt = 0
  while (s !== "1") {
    cnt += 1
    var cnt_zero = 0
    var cnt_one = 0
    for (let x of s) {
      if (x === "1") {
        cnt_one += 1
      } else {
        cnt_zero += 1
      }
    }
    zero += cnt_zero
    s = cnt_one.toString(2)
  }
  var answer = [cnt, zero]
  return answer
}