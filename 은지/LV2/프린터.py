def solution(priorities, location):
    answer = 0
    idx = [j for j in range(len(priorities))]
    x = priorities.pop(0)
    queue = [x]
    
    while queue:
        v = queue.pop(0)
        i = idx.pop(0)

        if len(priorities):
            max_v = max(priorities)
        else:
            return answer + 1

        if max_v > v:
            priorities.append(v)
            idx.append(i)
            x = priorities.pop(0)
            queue.append(x)
        else:
            if i == location:
                return answer + 1
            else:
                x = priorities.pop(0)
                queue.append(x)
                answer += 1
    return answer

p = [2, 1, 3, 2]
l = 1
print(solution(p, l))