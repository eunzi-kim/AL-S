import math
def solution(n):
    answer = -1
    nn = math.sqrt(float(n))
    if nn == int(nn):
        answer = (nn+1)**2
    return answer

print(solution(3))