function solution(skill, skill_trees) {
  var answer = 0
  for (let i = 0; i < skill_trees.length; i++) {
    var idx = 0
    var loop = true
    for (const j of skill_trees[i]) {
      if (skill.includes(j)) {
        if (skill[idx] != j) {
          loop = false
          break
        } else {
          idx += 1
        }
      } 
    }  
    if (loop) {
      answer += 1
    }
  }
  return answer
}

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)