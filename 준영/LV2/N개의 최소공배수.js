function gcd(a, b) {
  while (b > 0) {
    var temp = a % b
    a = b
    b = temp
  }
  return a
}

function lcm(a, b) {
  return a * b / gcd(a, b)
}

function solution(arr) {
  var answer = 0
  
  var temp = arr.slice()
  
  while (temp.length > 1) {
    var lcm_arr = Array(0)
    var x = temp[0]

    for (let i = 1; i < temp.length; i++) {
      lcm_arr.push(lcm(x, temp[i]))
    }
    temp = lcm_arr.slice()
  }

  answer = temp[0]
  return answer
}