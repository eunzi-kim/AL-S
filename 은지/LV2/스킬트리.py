def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        idx = -1 # 가장 최근에 사용된 skill 순서
        chk = 1 # skill 순서 체크
        for j in range(len(tree)):
            for i in range(len(skill)):
                if tree[j] == skill[i]:
                    if i != idx+1: # skill 순서 무시
                        chk = 0
                        break
                    else:
                        idx = i
        if chk == 1:  
            answer += 1
    return answer