function solution(n) {
  var arr = []
  for (let x of String(n)) {
    arr.push(x)
  }
  arr.sort((a, b) => b-a)
  const answer = Number(arr.join(""))
  return answer;
}