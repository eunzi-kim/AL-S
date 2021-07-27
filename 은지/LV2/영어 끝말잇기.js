function solution(n, words) {
  var answer = [0, 0];
  var past_lst = []
  var past = words[0][0]
  for (let i=0; i<words.length; i++) {    
    if (!past_lst.includes(words[i])) {
      past_lst.push(words[i])
    }
    else {
      answer = [i%n+1, parseInt(i/n)+1]
      break
    }

    if (past[past.length-1] !== words[i][0]) {
      answer = [i%n+1, parseInt(i/n)+1]
      break
    }
    past = words[i]
  }
  return answer;
}