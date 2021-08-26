function solution(priorities, location) {
  var answer = 0
  var temp = priorities.map((x, i) => [i, x])
  
  var result_stack = []

  while (temp.length) {
    var temp_x = temp.shift()
    var idx = temp_x[0]
    var x = temp_x[1]
    
    var is_possible = true

    for (const i of temp) {
      if (i[1] > x) {
        is_possible = false
        temp.push([idx, x])
        break
      }
    }

    if (is_possible) {
      result_stack.push(idx)
    }
  }
  answer = result_stack.indexOf(location) + 1
  return answer
}