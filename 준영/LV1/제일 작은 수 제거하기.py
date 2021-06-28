def solution(arr):
    x = min(arr)
    idx = arr.index(x)
    del arr[idx]
    answer = arr
    if len(answer) == 0:
        answer = [-1]
    return answer