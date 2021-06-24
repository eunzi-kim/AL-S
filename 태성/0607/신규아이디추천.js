const new_id = "...!@BaT#*..y.abcdefghijklm.."

function solution(new_id) {
  var answer = ''
  
  console.log(new_id)
  
  // 1단계
  answer = new_id.toLowerCase()
  
  // 2단계
  const chk = 'qwertyuiopasdfghjklzxcvbnm123456789-_.'
  let pre = []
  for (let a of answer) {
    if (chk.includes(a)) {
      pre.push(a)
    }
  }
  console.log(pre)
  
  
  // 3, 4 단계
  // 해당 코드는 맨 마지막 '.'을 뽑아내지 못하는데 어차피 빼줘야하니 문제 없으리라 판단
  let cnt = 0
  let pre1 = []
  for (let p of pre) {
    // console.log(p)
    if (p === '.') {
      cnt += 1
    } else {
      if (cnt >= 2) {
        pre1.push('.')
        pre1.push(p)
        cnt = 0
      } else {
        if (cnt === 1){
          pre1.push('.')
        }
        pre1.push(p)
        cnt = 0
      }
    }
  }
  
  console.log(pre1)
  
  // 4단계
  if (pre1[0] === '.') {
    pre1.splice(0, 1)
  }

  // 5단계
  if (pre1.length === 0) {
    pre1.push('a')
  }

  // console.log(pre1)

  // 6단계
  if (pre1.length >= 16) {
    pre1 = pre1.slice(0, 15)
    if (pre1[pre1.length-1] === '.') {
      pre1.pop()
    }
  }
  // console.log(pre1)

  // 7단계
  if (pre1.length === 1) {
    pre1.push(pre1[0])
    pre1.push(pre1[0])
  }

  if (pre1.length === 2) {
    pre1.push(pre1[1])
  }
  
  answer = pre1.join("")
  return answer
}



console.log(solution(new_id))