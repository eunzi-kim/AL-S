def solution(priorities, location):
    answer = 0
    idx = 0
    temp = []
    for i in priorities:
        temp.append([idx, i])
        idx += 1
        
    result_stack = []

    while temp:
        idx, x = temp.pop(0)
        is_possible = True
        for i in temp:
            if i[1] > x:
                is_possible = False
                temp.append([idx, x])
                break
        
        if is_possible:
            result_stack.append(idx)
    answer = result_stack.index(location)+1
    return answer