def solution(clothes):
    answer = 1
    sorts = {}
    for c in clothes:
        if c[1] in sorts:
            sorts[c[1]] += 1
        else:
            sorts[c[1]] = 1

    for sort in sorts:
        answer *= sorts[sort]+1
        
    answer -= 1

    return answer

# c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
c= [["a", "h"], ["b", "h"], ["c", "h"], ["d", "h"], ["e", "e"], ["f", "e"], ["g", "e"], ["h", "b"]]
print(solution(c))