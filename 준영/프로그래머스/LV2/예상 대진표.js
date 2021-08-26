function solution(n,a,b) {
  var answer = 1
  var a_seed = a % 2 ? parseInt(a / 2) + 1 : a / 2
  var b_seed = b % 2 ? parseInt(b / 2) + 1 : b / 2

  while (n != 1){
    if (a_seed === b_seed) break

    a_seed = a_seed % 2 ? parseInt(a_seed / 2) + 1 : a_seed / 2
    b_seed = b_seed % 2 ? parseInt(b_seed / 2) + 1 : b_seed / 2
    answer += 1
    n /= 2
  }
  return answer
}