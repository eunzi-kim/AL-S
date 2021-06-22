function solution(arr) {
  const min_v = Math.min(...arr)
  var idx = 0
  for (let i=0; i<arr.length; i++) {
    if (arr[i] === min_v) {
      idx = i
    }
  }
  arr.splice(idx, 1)
  if (arr.length == 0) {
    arr = [-1]
  }
  return arr;
}