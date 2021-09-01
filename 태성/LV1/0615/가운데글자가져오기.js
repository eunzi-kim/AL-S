const s = "abcde"	

function solution(s) {
  var answer = ''
  var m = parseInt(s.length/2)
  if (s.length % 2 === 1 ) {
    answer += s[m]
  } else {
    answer += s[m-1]
    answer += s[m]

  }
  return answer
}

console.log(solution(s))
