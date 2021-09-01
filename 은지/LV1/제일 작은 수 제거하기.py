def solution(arr):
    minV = min(arr)
    for i in range(len(arr)):
        if arr[i] == minV:
            arr.pop(i)
            break
    if len(arr) == 0:
        arr = [-1]
    return arr