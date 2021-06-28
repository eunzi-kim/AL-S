function solution(new_id) {
  var answer = ''
  var new_word = new_id.toLowerCase().replace(/[^\_\-\.\w]/g, "").replace(/\.+/g, ".").replace(/\B\.|\.\B/g, "")

  // 정규표현식 => 이메일 @ .com // 010-7610-8875 // 8633-3885

  if (new_word.length === 0) {
    new_word = "a"
  }

  new_word = new_word.slice(0, 15).replace(/\.\B/g, "")

  if  (new_word.length < 3) {
    const x = new_word.substr(new_word.length-1, 1)
    while (new_word.length < 3) {
      new_word += x
    }
  }

  answer = new_word
  return answer;
}

new_id = "...!@BaT#*..y.abcdefghijklm"	
console.log(solution(new_id))
new_id = "z-+.^."	
console.log(solution(new_id))
new_id = "=.="
console.log(solution(new_id))
new_id = "123_.def"
console.log(solution(new_id))
new_id = "abcdefghijklmn.p"	
console.log(solution(new_id))
new_id = "......a......a......a....."	
console.log(solution(new_id))
new_id = "-_.~!@#$%^&*()=+[{]}:?,<>/._-"	
console.log(solution(new_id))
new_id = "._._"	
console.log(solution(new_id))
