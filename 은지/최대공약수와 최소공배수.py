def solution(n, m):
    minV = min(n, m)
    maxV = max(n, m)
    for x in range(1, maxV*minV+1):
        # 최대공약수
        if minV % x == 0 and maxV % x == 0:
            g = x
        # 최소공배수
        if x % minV == 0 and x % maxV == 0:
            l = x
            break
    answer = [g, l]
    return answer

n = 3
m = 12
print(solution(n, m))