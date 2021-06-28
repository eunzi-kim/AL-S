def solution(x, n):
    answer = []
    temp = x
    for i in range(n):
        answer.append(temp)
        temp += x
    return answer