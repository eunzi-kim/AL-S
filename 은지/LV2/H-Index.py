def solution(citations):
    answer = 0
    for n in range(len(citations), -1, -1):
        h = 0
        for c in citations:
            if c >= n:
                h += 1
        if h >= n:
            answer = n
            break    
    return answer

c = [3, 0, 6, 1, 5]
print(solution(c))