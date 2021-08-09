function solution(skill, skill_trees) {
  var answer = 0;
  for (let tree of skill_trees) {
    var idx = -1
    var chk = 1
    for (let j=0; j<tree.length; j++) {
      for (let i=0; i<skill.length; i++) {
        if (tree[j] === skill[i]) {
          if (i !== idx + 1) {
            chk = 0
            break
          } else {
            idx = i
          }
        }
      }
    }
    if (chk === 1) {
      answer += 1
    }
  }
  return answer;
}