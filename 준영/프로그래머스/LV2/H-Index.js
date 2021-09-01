function solution(citations) {
  var answer = 0
  citations.sort((a, b) => a - b)
  for (let i = 0; i < citations.length; i++) {
    if (citations.length - i <= citations[i]) {
      answer = citations.length - i
      break
    }
  }
  return answer
}