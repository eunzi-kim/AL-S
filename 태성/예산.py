d = [2,2,3,3]

budget = 10

def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    cnt = 0
    for a in d:
        if budget - a >= 0:
            cnt += 1
            budget = budget - a

    answer = cnt


    return answer

print(solution(d, budget))
