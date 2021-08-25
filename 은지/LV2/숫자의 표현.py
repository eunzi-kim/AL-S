def solution(n):
    answer = 0
    for x in range(1, n+1):
        sub_a = 0
        while sub_a < n:
            sub_a += x
            x += 1
        if sub_a == n:
            answer += 1
    return answer