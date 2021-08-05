function solution(s) {
  var numbers = [];
  var sub = ""
  for (let v of s) {
    if (v !== " ") {
      sub += v
    } else {
      numbers.push(Number(sub))
      sub = ""
    }
  }
  numbers.push(Number(sub))
  var answer = String(Math.min(...numbers)) + " " + String(Math.max(...numbers))
  return answer;
}