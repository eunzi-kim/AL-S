def solution(arr):
    answer = 0
    for a in arr:
        answer += a

    answer = answer / len(arr)
    return answer