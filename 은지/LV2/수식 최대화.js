function solution(expression) {
  var answer = 0;
  var stack_n = []
  var stack_s = []
  var num = ""
  for (let e of expression) {
    if (e === "-") {
      stack_n.push(parseInt(num))
      num = ""
      stack_s.push(e)
    } else if (e === "+") {
      stack_n.push(parseInt(num))
      num = ""
      stack_s.push(e)
    } else if (e === "*") {
      stack_n.push(parseInt(num))
      num = ""
      stack_s.push(e)
    } else {
      num += e
    }
  }
  stack_n.push(parseInt(num))

  var symbol = [["*", "+", "-"], ["*", "-", "+"], ["+", "*", "-"], ["+", "-", "*"], ["-", "+", "*"], ["-", "*", "+"]]
  for (let v of symbol) {
    var stack_ss = stack_s.slice(0, stack_s.length)
    var stack_nn = stack_n.slice(0, stack_n.length)

    for (let j=0; j<3; j++) {
      var i = 0
      while (i < stack_ss.length) {
        if (stack_nn.length === 1) {
          break
        }
        if (stack_ss[i] === v[j]) {
          var w = parseInt(stack_nn.splice(i+1, 1))
          stack_ss.splice(i, 1)
          if (v[j] === "*") {
            stack_nn[i] = parseInt(stack_nn[i] * w)
          } else if (v[j] === "+") {
            stack_nn[i] = parseInt(stack_nn[i] + w)
          } else if (v[j] === "-") {
            stack_nn[i] = parseInt(stack_nn[i] - w)
          }
        } else {
          i += 1
        }
      }
    }
    if (answer < Math.abs(stack_nn[0])) {
      answer = Math.abs(stack_nn[0])
    }
  }
  return answer;
}

e = "200-300-500-600*40+500+500"
console.log(solution(e))