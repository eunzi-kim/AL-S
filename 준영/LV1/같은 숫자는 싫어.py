def solution(arr):
    answer = []
    answer.append(arr[0])
    idx = 0
    for i in arr:
        if answer[idx] != i:
            answer.append(i)
            idx += 1
    return answer