function solution(arr) {
  while (arr.length > 1) {
    var a = arr.shift()
    var b = arr.shift()
    var v = Math.min(a, b)
    var gcd = v
    for (let x=1; x<=v; x++) {
      if (a%x === 0 && b%x === 0) {
        gcd = x
      }
    }
    arr.push(parseInt((a*b)/gcd))
  }
  return arr[0];
}