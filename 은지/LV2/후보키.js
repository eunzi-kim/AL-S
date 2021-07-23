function solution(relation) {
  var answer = 0;
  var n = relation[0].length
  var m = relation.length

  var cases = []
  for (let i=0; i<(1<<n); i++) {
    var sub_l = []
    for (let j=0; j<n; j++) {
      if (i & (1 << j)) {
        sub_l.push(j)
      }
    }
    cases.push(sub_l)
  }
  cases.shift()
  
  var i = 0
  while (i < cases.length) {
    var v = cases[i]
    var chk = []
    for (let k=0; k<m; k++) {
      var sub_c = ""
      for (let j of v) {
        sub_c += relation[k][j]
      }
 
      if (!chk.includes(sub_c)) {
        chk.push(sub_c)
      }
    }

    if (chk.length === m) {
      var k = i+1
      while (k < cases.length) {
        var cnt = 0
        for (let w of cases[i]) {
          if (cases[k].includes(w)) {
            cnt += 1
          }
        }
        if (cnt === cases[i].length) {
          cases.splice(k, 1)
        } 
        else {
          k += 1
        }
      }
      i += 1
    }
    else {
      cases.splice(i, 1)
    }
  }
  return cases.length;
}

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
console.log(solution(relation))