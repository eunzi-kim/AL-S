function solution(s) {
  var answer = []
  var arr = s.split('},')
  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i].replace(/{+/, '')
    arr[i] = arr[i].replace(/}+/, '')
    arr[i] = arr[i].split(',').map(Number)
  }

  arr.sort((a, b) => a.length - b.length)

  var cnt_arr = Array(100001).fill(0)

  for (const i of arr) {
    for (const j of i) {
      if (cnt_arr[j] === 0) {
        cnt_arr[j] = 1
        answer.push(j)
      }
    }
  }
  return answer
}