function solution(new_id) {
  var answer = '';
  const exam = 'qwertyuiopasdfghjklzxcvbnm0123456789._-'
  var lst_a = []
  var cnt = 0
  // 1단계
  const id = new_id.toLowerCase()
  for (let x of id) {
    // 2단계
    if (exam.indexOf(x) != -1) {
      // 3단계
      if (x === '.') {
        cnt += 1
      } else {
        cnt = 0
      }
      if (cnt <= 1) {
        lst_a.push(x)
      }
    }
  }
  // 4단계
  if (lst_a.length > 0 && lst_a[0] === '.') {
    lst_a.shift()
  }
  if (lst_a.length > 0 && lst_a[lst_a.length-1] === '.') {
    lst_a.pop()
  }
  // 5단계
  if (lst_a.length === 0) {
    lst_a.push('a')
  }
  // 6단계
  if (lst_a.length >= 16) {
    lst_a = lst_a.slice(0, 15)
    if (lst_a[14] == '.') {
      lst_a.pop()
    }
  }
  // 7단계
  if (lst_a.length === 1) {
    lst_a.push(lst_a[0])
    lst_a.push(lst_a[0])
  }
  else if (lst_a.length === 2) {
    lst_a.push(lst_a[1])
  }
  // 배열 => 문자열 변환
  answer = lst_a.join('')
  return answer;
}