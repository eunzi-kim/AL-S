import copy

def solution(n,a,b):
    answer = 0
    person = [x for x in range(1, n+1)]
    while person:
        winner = []
        for i in range(0, len(person), 2):
            p1 = person[i]
            p2 = person[i+1]
            if p1 == a or p2 == b:
                if p1 == a and p2 == b:
                    return answer + 1
                elif p2 != b:
                    winner.append(p1)
                elif p1 != a:
                    winner.append(p2)
            elif p1 == b or p2 == a:
                if p1 == b and p2 == a:
                    return answer + 1
                elif p2 != a:
                    winner.append(p1)
                elif p1 != b:
                    winner.append(p2)
            else:
                winner.append(p1)
        person = copy.deepcopy(winner)
        answer += 1
    return answer

n = 8
a = 4
b = 7
print(solution(n, a, b))