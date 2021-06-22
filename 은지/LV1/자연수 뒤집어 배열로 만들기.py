def solution(n):
    answer = []
    while n > 0:
        v = n % 10
        answer.append(v)
        n //= 10
    return answer