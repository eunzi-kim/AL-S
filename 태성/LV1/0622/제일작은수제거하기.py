def solution(arr):
    min_v = min(arr)

    for i in range(len(arr)):
        if min_v == arr[i]:
            arr.pop(i)
            break
    if not arr:
        arr.append(-1)
    return arr