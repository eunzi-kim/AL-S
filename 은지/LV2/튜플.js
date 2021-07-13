function solution(s) {
  var answer = [];
  var n_lst = []
  for (let i=0; i<=100001; i++) {
    n_lst.push(0)
  }
  var num = ""
  for (let i=0; i<s.length; i++) {
    if (s[i] !== "{" && s[i] !== "}" && s[i] !== ",") {
      num += s[i]
    } else if (num.length) {
      n_lst[Number(num)] += 1
      num = ""
    }
  }

  var lst = []
  for (let i=0; i<100001; i++) {
    if (n_lst[i]) {
      lst.push([n_lst[i], i])
    }
  }
  lst.sort((a, b) => b[0]-a[0])
  for (let x of lst) {
    answer.push(x[1])
  }
  return answer;
}

s = "{{20,111},{111}}"
console.log(solution(s))