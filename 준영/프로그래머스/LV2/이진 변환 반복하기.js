function solution(s) {
  var answer = [];
  var cnt = 0
  var zero_cnt = 0

  var s_arr = s.split('').map(Number)
  
  while (s_arr.length > 1) {
    var idx = 0

    while (s_arr.length > idx) {
      if (s_arr[idx] === 0) {
        s_arr.splice(idx, 1)
        zero_cnt += 1
      } else {
        idx += 1
      }
    }

    var n = s_arr.length

    var new_arr = []
    var new_s = ''

    while (n) {
      // new_arr.push(n % 2)
      new_s += String(n % 2)
      n = parseInt(n / 2)
    }
    new_arr = new_s.split('').map(Number)
    s_arr = new_arr

    cnt += 1
  }
  answer = [cnt, zero_cnt]
  return answer
}

s = "110010101001"
solution(s)