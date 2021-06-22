def solution(n):
    answer = -1
    if n ** (0.5) == int(n ** (0.5)):
        answer = (int(n ** (0.5)) + 1) ** 2
    return answer