function solution(priorities, location) {
  var answer = 0;
  var idx = []
  for (let j=0; j<priorities.length; j++) {
    idx.push(j)
  }
  var x = priorities.shift()
  var queue = [x]

  while (queue.length > 0) {
    var v = queue.shift()
    var i = idx.shift()

    if (priorities.length) {
      var max_v = Math.max(...priorities)
    } else {
      return answer + 1
    }
    
    if (max_v > v) {
      priorities.push(v)
      idx.push(i)
      x = priorities.shift()
      queue.push(x)
    } else {
      if (i === location) {
        return answer + 1
      } else {
        x = priorities.shift()
        queue.push(x)
        answer += 1
      }
    }
  }
  return answer;
}