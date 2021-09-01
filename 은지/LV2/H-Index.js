function solution(citations) {
  var answer = 0;
  for (let n=citations.length; n>=0; n--) {
    var h = 0
    for (let c of citations) {
      if (c >= n) {
        h += 1
      }
    }
    if (h >= n) {
      answer = n
      break
    }
  }
  return answer;
}