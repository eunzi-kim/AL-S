def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        idx = 0
        for i in st:
            if i in skill:
                if skill[idx] != i:
                    break
                else:
                    idx += 1
        else:
            answer += 1
        
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)