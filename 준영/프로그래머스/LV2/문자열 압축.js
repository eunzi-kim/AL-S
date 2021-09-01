function solution(s) {
  var answer = s.length

  for (let i = 1; i <= parseInt((s.length)/2); i++) {
    var def_str = ''
    var def_n = 1
    var temp = s.slice(0, i)
    var k = 0
    
    for (let j = i; j <= s.length; j += i) {
      k = j
      if (temp === s.slice(j, j+i)) {
        if (def_n === 1) {
          def_str += temp
        } else {
          def_str += String(def_n)
          def_str += temp
          def_n = 1
        }
        temp = s.slice(j, j+i)
        console.log(temp)
      } else {
        def_n += 1
      }
    }
    def_str += s.slice(k, s.length)
    if (def_str.length < answer) {
      answer = def_str.length
    }
    console.log(def_str)
  }

  return answer;
}

solution('ababcdcdababcdcd')
// solution('abcbc')
