def solution(n):
    answer = 0
    temp = n ** 0.5
    if temp.is_integer():
        answer = (temp + 1) ** 2
    else:
        answer = -1
    return answer