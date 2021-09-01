function chk(l) {
  var lst = l.slice(0, l.length)
  var i = 0
  while (i < lst.length-1) {
    if (lst[i] === "(" && lst[i+1] === ")") {
      lst.splice(i, 2)
      if (i > 0) {
        i -= 1 
      }
    }
    else if (lst[i] === "{" && lst[i+1] === "}") {
      lst.splice(i, 2)
      if (i > 0) {
        i -= 1 
      }
    }
    else if (lst[i] === "[" && lst[i+1] === "]") {
      lst.splice(i, 2)
      if (i > 0) {
        i -= 1 
      }
    }
    else {
      i += 1
    }
  }
  return lst.length
}

function solution(s) {
  var answer = 0;
  var lst_s = []
  for (let x of s) {
    lst_s.push(x)
  }

  for (let i=0; i<s.length; i++) {
    if (chk(lst_s) === 0) {
      answer += 1
    }
    var v = lst_s.shift()
    lst_s.push(v)
  }
  return answer;
}