const dartResult = "1D2S#10S"

function solution(dartResult) {
  var answer = 0;
  var pre = []
  var tmp = ""
  const chk_list = ["S", "D", "T", "#", "*"]
  for (let d of dartResult) {
    // console.log(d)
    if (chk_list.includes(d)) {
      if (tmp.length > 0) {
        pre.push(parseInt(tmp))
        tmp = ""
        // console.log(pre)
      }
      // console.log(d)
      pre.push(d)
    } else{
      // pre.push(d)
      tmp += d
    }
    // console.log(tmp)
  }

  console.log(pre)

  var array = []
  for (let p of pre) {
    // console.log("p")
    if (chk_list.includes(p)) {
      console.log(p)
      if (p === "S") {
        var s = array.pop()
        array.push(s)
      } else if (p === "D") {
        var dd = array.pop()
        console.log(dd)
        array.push(dd*dd)
        console.log(array)
      } else if (p === "T") {
        var tt = array.pop()
        array.push(tt*tt*tt)
      } else if (p === "*") {
        if (array.length === 1) {
          var star = array.pop()
          array.push(star*2)
        } else if (array.length === 2) {
          var star_2 = array.pop()
          var star_1 = array.pop()

          array.push(star_1*2)
          array.push(star_2*2)
        }
      } else if (p === "#") {
        var mm = array.pop()
        array.push(mm*(-1))
        
      }
    } else {
      console.log("숫자")
      console.log(array)
      if (array.length < 2) {
        array.push(p)
        console.log(array)
      } else if (array.length === 2) {
        answer += array.shift()
        console.log(answer)
        console.log(array)
        array.push(p)
        console.log(array)
      }
    }
  }
  for (let a of array) {
    console.log(answer)
    answer += a
  }
  console.log(answer)
  return answer;
}


solution(dartResult)