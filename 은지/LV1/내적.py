def solution(a, b):
    answer = 0
    N = len(a)
    for i in range(N):
        answer += a[i] * b[i]
    return answer