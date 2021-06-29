function solution(s)
{
    var answer = 0;
    var stack = []
    for (let x of s) {
      if (stack.length) {
        var v = stack.pop()
        if (x !== v) {
          stack.push(v)
          stack.push(x)
        }
      } else {
        stack.push(x)
      }
    }
    if (stack.length === 0) {
      answer = 1
    }
    return answer;
}

s = "baabaa"
console.log(solution(s))