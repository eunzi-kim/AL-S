function solution(n, words) {
  var answer = [0, 0]
  var word_dict = [words[0]]
  var idx = 1
  while (idx < words.length) {
    if (word_dict[word_dict.length-1].substr(word_dict[word_dict.length-1].length-1, 1) != words[idx].substr(0, 1) || word_dict.includes(words[idx])) {
      answer[0] = (idx % n) + 1
      answer[1] = parseInt(idx / n) + 1
      break
    } else {
      word_dict.push(words[idx])
    }
    idx += 1
  }
  return answer
}