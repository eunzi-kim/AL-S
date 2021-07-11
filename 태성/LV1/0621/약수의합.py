def solution(n):
    answer = 0
    array = list(range(1, n + 1))

    for a in array:
        if n % a == 0:
            answer += a
    return answer