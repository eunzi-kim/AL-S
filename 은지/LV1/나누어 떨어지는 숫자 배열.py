def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    if len(answer):
        answer.sort()
    else:
        answer = [-1]
    return answer